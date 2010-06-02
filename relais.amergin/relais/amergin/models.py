#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from datetime import datetime

from django.utils.encoding import smart_str
from django.db import models
from django.forms import widgets

from relais.core.config import (
	BIOSEQ_TYPE_VOCAB,
	BIOSEQ_ALPHABET_AMINOACID_LETTERS,
	BIOSEQ_ALPHABET_NUCLEOTIDE_LETTERS,
)

from relais.amergin import morefields


### CONSTANTS & DEFINES ###

# format for UIDs
UID_DATETIME_FMT = "%Y%m%d-%H%M%S"
UID_BASE = 0


### IMPLEMENTATION ###

BIOSEQ_TYPE_CHOICES = [[x, x.lower()] for x in BIOSEQ_TYPE_VOCAB]


### UTILITIES

def generate_uid (prefix="uid"):
	"""
	Generate a unique identifer for this record.
	"""
	global UID_BASE
	UID_BASE += 1
	date_str = datetime.now().strftime ("%Y%m%d-%H%M%S")
	return u"%s.%s.%s" % (prefix, date_str, UID_BASE)
	
	
def create_identifier(id_prefix="", help_text=None):
	init_val_fn = lambda: generate_uid (id_prefix)
	return models.CharField(
		max_length=32,
		primary_key=True,
		help_text="""A unique identifier for the record. If not supplied, one
			will be generated. It cannot be changed after object creation.""",
	)

def create_internal_identifier(id_prefix=""):
	init_val_fn = lambda: generate_uid (id_prefix)
	return models.CharField(
		max_length=32,
		primary_key=True,
		#help_text="Not editable by user",
	)
	
def create_title (help_text=None):
	return models.CharField (
		max_length=72,
		blank=True,
		help_text="""A user friendly name for the record. This is optional and
			need not be unique.""",
	)
	
def create_description (help_text=None):
	return models.TextField(
		blank=True,
		help_text="""Notes on or a summary of the record.. This is optional and
			need not be unique.""",
	)
	
def create_source(help_text=None):
	return models.CharField(
		max_length=32,
		blank=True,
		help_text="""The originating authority for this record. We suggest that
			it be the database name (e.g. 'genbank') or a reverse-url naming
			of the institute (e.g. 'uk.ac.iah.btv').""",
	)
	


### ABSTRACT BASE MODELS

class BasePrimaryModel (models.Model):
	"""
	A base class for primary (standalone) database objects.
	"""
			
	class Meta:
		abstract = True
		managed = False		  
		ordering = ['title', 'identifier']
	
	def __str__(self):
		return smart_str (self.get_name())
		
	def get_name (self):
		"""
		Return a nicely formatted string of the title and id.
		
		This generates a nice moniker for the record for presentation purposes,
		in the form "title (id)", accounting for either or both of those fields being
		missing. It is not intended to be a unique identifier.
		
		:Returns:
			A unicode string of the title and id, or an empty string if neither
			is available.
		
		For example::
		
			>>> n1 = NamedRelaisObject()
			>>> n1.get_name()
			''
			>>> n1.title = ' My title! '
			>>> n1.get_name()
			'My title!'
			>>> n1.identifier = ' an id'
			>>> n1.get_name()
			'My title! (an id)'
		
		"""
		if (self.title and self.identifier and (self.title != self.identifier)):
			return u'%s (%s)' % (self.title.strip(), self.identifier.strip())
		elif (self.title):
			return unicode (self.title.strip())
		elif (self.identifier):
			return unicode (self.identifier.strip())
		else:
			return u''

	@classmethod
	def generate_uid (cls):
		return generate_uid (cls.uid_prefix)


class BaseSecondaryModel (models.Model):
	def __str__(self):
		return smart_str(self.identifier)

	@classmethod
	def generate_uid (cls):
		return generate_uid (cls.uid_prefix)
		
	class Meta:
		abstract = True
		managed = False		  
		ordering = ['identifier']


### DOMAIN MODELS

class Bioseq (BasePrimaryModel):
	identifier = create_identifier (id_prefix="bseq")
	title = create_title()
	description = create_description()
	source = create_source()
	seqtype = models.CharField ('Type',
		max_length=32,
		blank=False,
		choices=BIOSEQ_TYPE_CHOICES,
		default=BIOSEQ_TYPE_CHOICES[0][0],
		help_text='Protein or DNA?',
	)
	seqdata = models.TextField ('Sequence data',
		help_text="""The raw sequence data. The standard IUPAC alphabet should be
			used, i.e. %s for nucleotide or %s for protein""" % (
				BIOSEQ_ALPHABET_NUCLEOTIDE_LETTERS, BIOSEQ_ALPHABET_NUCLEOTIDE_LETTERS),
		blank=False,
	)
	sample_id = models.CharField(max_length=32, blank=True)

	uid_prefix = 'bseq'	
	
	class Meta:
		db_table = u'biosequences'
		verbose_name = 'biosequence'
		verbose_name_plural = 'biosequences'


class BioseqAnnotation (BaseSecondaryModel):
	identifier = create_internal_identifier (id_prefix="bsan")
	name = models.CharField (max_length=32, blank=False)
	value = models.TextField (blank=False)
	biosequence = models.ForeignKey (Bioseq, related_name="annotations")
	
	uid_prefix = 'bsan'
	
	class Meta:
		db_table = u'bioseqannotations'

	
class BioseqCollection (BasePrimaryModel):
	identifier = create_identifier (id_prefix="bcol")
	title = create_title()
	description = create_description()
	source = create_source()
	members = models.ManyToManyField (Bioseq, through='BioseqCollectionMembership')
	
	uid_prefix = 'bcol'

	class Meta:
		db_table = u'bioseqcollections'
		verbose_name = 'bioseq collection'
		verbose_name_plural = 'bioseq collections'


class BioseqCollectionMembership (models.Model):
	collection = models.ForeignKey (BioseqCollection)
	biosequence = models.ForeignKey (Bioseq)
	
	class Meta:
		db_table = u'bioseqcollections_biosequences'
		managed = False		  

	def __str__(self):
		return smart_str (self.biosequence.get_name())


class BioseqFeature (BaseSecondaryModel):
	identifier = create_internal_identifier (id_prefix="bsft")
	location = models.CharField(max_length=32, blank=True)
	type = models.CharField(max_length=32, blank=True)
	biosequence = models.ForeignKey (Bioseq, related_name="features")

	uid_prefix = 'bsft'
	
	class Meta:
		db_table = u'bioseqfeatures'


class BioseqQualifier (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	name = models.CharField(max_length=32, blank=True)
	value = models.TextField(blank=True)
	seqfeature_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'bioseqqualifiers'
		 
		 
		 
		 


class Assay (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = create_title()
	description = create_description()
	source = create_source()
	type = models.CharField(max_length=32, blank=True)
	format = models.CharField(max_length=32, blank=True)
	results = models.TextField(blank=True)
	sample_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'assays'


class BioseqExtref (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	urn = models.CharField(max_length=72, blank=True)
	biosequence_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'bioseqextrefs'





class Document (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = create_title()
	description = create_description()
	source = create_source()
	filename = models.CharField(max_length=72, blank=True)
	fileformat = models.CharField(max_length=32, blank=True)
	content = models.TextField(blank=True) # This field type is a guess.
	sample_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'documents'

class Region (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = create_title()
	description = create_description()
	synonyms = models.TextField(blank=True)
	centroid_lat = models.TextField(blank=True) # This field type is a guess.
	centroid_lon = models.TextField(blank=True) # This field type is a guess.
	type = models.CharField(max_length=32, blank=True)
	within_region_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'regions'

class Sample (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = create_title()
	description = create_description()
	source = create_source()
	locn_lat = models.TextField(blank=True) # This field type is a guess.
	locn_lon = models.TextField(blank=True) # This field type is a guess.
	locn_method = models.CharField(max_length=32, blank=True)
	address = models.TextField(blank=True)
	country = models.CharField(max_length=72, blank=True)
	region_id = models.CharField(max_length=32, blank=True)
	date_collected = models.DateTimeField(null=True, blank=True)
	date_collected_exact = models.NullBooleanField(null=True, blank=True)
	date_received = models.DateTimeField(null=True, blank=True)
	final_result = models.CharField(max_length=32, blank=True)
	host = models.CharField(max_length=32, blank=True)
	status = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'samples'
