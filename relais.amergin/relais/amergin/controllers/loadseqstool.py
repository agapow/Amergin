#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for controllers that are tool forms.

"""

### IMPORTS ###

import exceptions

from django import forms
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from relais.iah.btv.annotatedseqreader import (AnnotatedSeqReader,
   annotated_seqrec_to_bioseq)
from relais.core.bpcompat.seqrecreader import SeqrecReader
from relais.core.bpcompat.convert import bp_seqrec_to_bioseq

from toolcontroller import ToolController
from relais.amergin import messages, models
from relais.amergin.dev import *


### CONSTANTS & DEFINES ###

FILETYPE_TO_EXTS = {
	'fasta': ['fa', 'fas'],
	'genbank': ['gb'],
	'stockholm': ['sth'],
}

EXT_TO_FILETYPE = {}
for k,v in FILETYPE_TO_EXTS.iteritems():
	EXT_TO_FILETYPE[k] = k
	for ext in v:
		EXT_TO_FILETYPE[ext] = k


### IMPLEMENTATION ###

# deduce file format from name
def guess_format (file_name):
	ext = file_name.lower().split('.')[-1]
	return EXT_TO_FILETYPE.get (ext, None)
	

def seqrec_to_relaisbioseq (seqrec):
	"""
	Transform a Seqrecord with added fields into an Amergin bioseq.
	"""
	if seqrec.annotations.has_key ('identifier'):
			  seqrec.id = seqrec.annotations ['identifier']
			  del seqrec.annotations ['identifier']
	if seqrec.annotations.has_key ('title'):
			  seqrec.name = seqrec.annotations ['title']
			  del seqrec.annotations ['title']
	return bp_seqrec_to_bioseq (seqrec, True, True)
	
	
def relaisbioseq_to_djbioseq (am):
	"""
	Create a Django biosequence from an Amergin one
	"""
	# TODO: needs to translate qualifiers
	dj = models.Bioseq()
	dj.identifier = am.identifier
	dj.title = am.title
	dj.description = am.description
	dj.source = am.source
	dj.seqtype = am.seqtype
	dj.seqdata = am.seqdata
	for a in am.annotations:
		new_ann = models.BioseqAnnotation()
		new_ann.name = a.name
		new_ann.value = a.value
		new_ann.identifier = models.BioseqAnnotation.generate_uid()
		dj.annotations.add (new_ann)
	for f in am.features:
		new_feat = models.BioseqFeature()
		new_feat.type = f.type
		new_feat.location = f.seqlocation
		new_feat.identifier = models.BioseqFeature.generate_uid()
		dj.features.add (new_feat)
	return dj
	

class LoadSeqsTool (ToolController):
	"""
	"""
	actions = [
		('upload','upload sequences'),
	]
	fieldsets = [
		['Source', 'seqfile', 'use_ann_reader', 'format'],
		['Labelling', 'bseq_src', 'bseq_desc', 'extra_ann'],
		['Collect uploads', 'make_collection', 'collection_title',
			'collection_desc', 'collection_src'],
	]	
	fallback_template = "relais.amergin/model.html"
	
	def __init__ (self):
		ToolController.__init__ (self,
			identifier='loadseqs',
			description="""Perform a bulk upload of biosequences from a single
				file to the repository. A collection can be formed from the
				contents.""",
			title="Load biosequences",
		)

	def render (self, request, *args, **kwargs):
		if (request.user.is_staff):
			return ToolController.render (self, request, *args, **kwargs)
		else:
			return HttpResponse("Only admins have access to this tool.")

	
	
	def process_form (self, data):
		# NOTE: must override this in derived class
		## Preconditions & preparation:
		msgs = []
		results = []
		## Main:
		
		try:
			upfile = data['seqfile']
			# deduce format and make reader
			if data['format'] != 'auto':
				format = data['format']
			else:
				format = guess_format(upfile.name)
				if not format:
					raise exceptions.ValueError ("can't guess format from file name")
			# TODO: because SeqrecReader isn't iterable
			if data[u'use_ann_reader']:
				reader = AnnotatedSeqReader (upfile, format)
			else:
				reader = SeqrecReader (upfile, format).read()
			#reader = reader_cls (upfile, format)
			
			# read it! we have to do a fugly seqrec -> relais bseqs -> amergin bseqs
			if data['extra_ann']:
				ann_key, ann_val = [x.strip() for x in data['annotation'].split(':', 1)]
			inseqs = []
			for seqrec in reader:
				if data['bseq_src']:
					seqrec.source = data['source']
				if data['bseq_desc']:
					seqrec.description = data['description']
				if data['extra_ann']:
					seqrec.annotations[ann_key.lowercase()] = ann_val
				bioseq = seqrec_to_relaisbioseq (seqrec)
				inseqs.append (bioseq)
				
			# load seqs and make collection
			dj_bseqs = [relaisbioseq_to_djbioseq (x) for x in inseqs]
			print ("djseq\n")
			pp (dj_bseqs[0].annotations.count())
			pp (dj_bseqs[0].features.count())
			if data['overwrite_bseqs']:
				seqs_to_write = dj_bseqs
				unwritten_seqs = None
			else:
				seqs_to_write = []
				unwritten_seqs = []
				for s in dj_bseqs:
					try:
						listing = models.Bioseq.objects.get(pk=s.identifier)
						unwritten_seqs.append (s.identifier)
					except:
						seqs_to_write.append (s)
			
			if unwritten_seqs:
				msgs.append (messages.Info ("""The following sequences already
					exist in the database and were not overwritten: %s""" %
					', '.join (unwritten_seqs)))
			if seqs_to_write:
				for s in seqs_to_write:
					s.save()
				msgs.append (messages.Success ("%s sequences were uploaded." %
					len (seqs_to_write)))
				if data['make_collection']:
					new_coll = models.BioseqCollection()
					if data['collection_title']:
						new_coll.title = data['collection_title']
					if data['collection_desc']:
						new_coll.description = data['collection_desc']
					if data['collection_src']:
						new_coll.source = data['collection_src']
					new_coll.identifier = models.BioseqCollection.generate_uid()
					new_coll.save()
					for s in seqs_to_write:
						membership = models.BioseqCollectionMembership()
						membership.collection = new_coll
						membership.biosequence = s
						membership.save()

			else:
				msgs.append (messages.Error ("No sequences were uploaded."))
				
		except exceptions.StandardError, err:
			print "Problem with '%s': %s" % (upfile.name, err)
			msgs.append (messages.Error ("Problem with '%s': %s" % (upfile.name, err)))
			raise
		except:
			print "Problem with '%s': %s" % (upfile.name, 'unknown')
			msgs.append (messages.Error ("Problem with '%s': %s" % (upfile.name, 'unknown')))
			raise
		
		## Postconditions & returns
		return msgs, results
	
	# NOTE: must override this in derived class
	class ToolForm (forms.Form):
		seqfile = forms.FileField(
			label="Sequence file",
			help_text="A file containing an alignment or multiple sequences.",
		)
		use_ann_reader = forms.BooleanField(
			label="Use extended reader",
			help_text="""Interprete directions embedded in
				the comments or description section of a sequence
				as annotations in the resultant sequence.""",
			initial=False,
			required=False,
		)
		format = forms.ChoiceField(
			label="Sequence format",
			required=True,
			choices=[
				# val, label
				["auto", "Auto-detect"],
				["fasta", "Fasta"],
				["genbank", "Genbank"],				
			],
			help_text="""If not given, the format will be guessed from the file
				name. Currently recognised file types are: <tt>%s</tt>""" % \
				' '.join (sorted (EXT_TO_FILETYPE.keys())),
		)
		bseq_src = forms.CharField(
			label="Source",
			help_text="""Label any uploaded sequence with the supplied
				source. If the sequence already has a source, it will be
				overwritten.""",
			required=False,
			max_length=100,
		)
		bseq_desc = forms.CharField(
			label="Description",
			help_text="""This will label any uploaded sequence with the supplied
				description. If the sequence already has a source, it will be
				overwritten.""",
			required=False,
			max_length=100,
		)
		extra_ann = forms.CharField(
			label="Add annotation",
			help_text="""This will tag any uploaded sequence with the supplied
				annotation. Write this as 'key:value'. If the sequence already has
				a value for that annotation, it will be overwritten.""",
			required=False,
			max_length=100,
		)
		overwrite_bseqs = forms.BooleanField(
			label="Overwrite biosequences",
			help_text="Replace any prexisting sequences with the same identifier.",
			initial=False,
			required=False,
		)

		make_collection = forms.BooleanField(
			label="Make collection",
			help_text="""Form a collection from the contents of this upload. The
				collection will """,
			initial=False,
			required=False,
		)
		collection_title = forms.CharField(
			label="Collection title",
			required=False,
			max_length=100,
		)
		collection_desc = forms.CharField(
			label="Collection description",
			required=False,
			max_length=100,
		)
		collection_src = forms.CharField(
			label="Collection source",
			required=False,
			max_length=100,
		)
