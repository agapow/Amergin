#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from django import forms

from relais.iah.btv.annotatedseqreader import (AnnotatedSeqReader,
   annotated_seqrec_to_bioseq)
from relais.core.bpcompat.seqrecreader import SeqrecReader
from relais.core.bpcompat.convert import bp_seqrec_to_bioseq
 
from basetool import BaseTool
from registry import register_tool
from relais.amergin import messages

__all__ = [
]


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
	ext = file_name.lowercase().split('.')[-1]
	return EXT_TO_FILE.get (ext, None)
	

def seqrec_to_ambioseq (seqrec):
	"""
	Transform a Seqrecord with added fields into an Amergin bioseq.
	"""
	if seqrec.annotations.has_key ('identifier'):
			  seqrec.id = seqrec.annotations ['identifier']
			  del seqrec.annotations ['identifier']
	if seqrec.annotations.has_key ('title'):
			  seqrec.name = seqrec.annotations ['title']
			  del seqrec.annotations ['title']
	rel_bseq = convert.bp_seqrec_to_bioseq (seqrec, True, True)


	
class LoadSeqsTool (BaseTool):
	identifier = "loadbseqs"
	title = "Load biosequences"
	description = """Perform a bulk upload of biosequences from a single file
		to the repository. A collection can be formed from the contents."""
	template = "tool.html"
	actions = [
		('upload','upload sequences'),
	]
	fieldsets = [
		['Source', 'seqfile', 'use_ann_reader', 'format'],
		['Labelling', 'bseq_src', 'bseq_desc', 'extra_ann'],
		['Collect uploads', 'make_collection', 'collection_title',
			'collection_desc', 'collection_src'],
	]
	
	
	def process_form (data):
		try:
			upfile = data['seqfile']
			# deduce format and make reader
			if data['format'] != 'auto':
				format = data['format']
			else:
				format = guess_format(upfile.name)
			if data[u'use_ann_reader']:
				reader_cls = AnnotatedSeqReader
			else:
				reader_cls = SeqrecReader
			reader = reader_cls (upfile, format)
			
			# read it! we have to do a fugly seqrec -> relais bseqs -> amergin bseqs
			inseqs = []
			for seqrec in reader:
				if data['source']:
					seqrec.source = data['source']
				if data['description']:
					seqrec.description = data['description']
				if data['annotation']:
					ann_key, ann_val = [x.strip() for x in data['annotation'].split(':', 1)]
					seqrec.annotations[ann_key.lowercase()] = ann_val
				bioseq = seqrec_to_ambioseq (seqrec)
				inseqs.append (bioseq)
				
			# load seqs and make collection
			#overwrite_bseqs = forms.BooleanField(
			#make_collection = forms.BooleanField(
			#collection_title = forms.CharField(
			#collection_desc = forms.CharField(
			#collection_src = forms.CharField(
				
		except exceptions.StandardError, err:
			print "Problem with '%s': %s" % (f, err)
		except:
			print "Problem with '%s': %s" % (f, 'unknown')


	class ToolForm(forms.Form):
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
				annotation. If the sequence already has a value for that annotation,
				it will be overwritten.""",
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
				collection will have the details given below.""",
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

	
register_tool (LoadSeqsTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
