#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION

"""

### IMPORTS ###

import re

from models import *
from django.contrib import admin
from django.forms import widgets
from django import forms
from django.conf import settings

from relais.core.config import (
	BIOSEQ_TYPE_VOCAB,
	BIOSEQ_ALPHABET_AMINOACID_LETTERS,
	BIOSEQ_ALPHABET_NUCLEOTIDE_LETTERS,
)


### CONSTANTS & DEFINES ###

WHITESPACE_REGEX = re.compile (r'\s+')


### IMPLEMENTATION ###

### UTILITIES


### BASE ADMIN FORMS

class PrimaryObjectAdminForm (forms.ModelForm):
	"""
	A common base form for editting primary objects.
	"""
	
	# NOTE: derived classes _must_ define model in Meta
		
	def __init__ (self, *args, **kwargs):
		forms.ModelForm.__init__(self, *args, **kwargs)
		self.fields['identifier'].required = False
		instance = getattr(self, 'instance', None)
		if instance and instance.identifier:
			self.fields['identifier'].widget.attrs['readonly'] = True
	
	def clean_identifier (self):
		raw_id = self.cleaned_data['identifier']
		return (raw_id or self.__class__.Meta.model.generate_uid()).strip()

	def clean_title (self):
		return self.cleaned_data['title'].strip()
		
	def clean_description (self):
		return self.cleaned_data['description'].strip()
		
	def clean_source (self):
		return self.cleaned_data['source'].strip()


class SecondaryObjectAdminForm (forms.ModelForm):
	"""
	A common base form for editting secondary objects.
	"""
	
	# NOTE: derived classes _must_ define model in Meta
		
	# the identifier should be autogenerated at creation
		
	def __init__ (self, *args, **kwargs):
		forms.ModelForm.__init__ (self, *args, **kwargs)
		uid_field = self.fields['identifier']
		uid_field.required = False
		uid_field.widget.attrs['readonly'] = True
		uid_field.widget.attrs['placeholder'] = "not editable"
	
	def clean_identifier (self):
		raw_id = self.cleaned_data['identifier']
		return raw_id or raw_id.strip() or self.__class__.Meta.model.generate_uid()


class BasePrimaryObjectAdmin (admin.ModelAdmin):
	search_fields = ['identifier', 'title', 'description', 'source']
	
	class Media:
		css = {
			"all": (settings.MEDIA_URL + "/relais.amergin/css/admin.css",)
		}
		js = (
		#	"my_code.js",
		)

class BaseSecondaryObjectAdmin (admin.ModelAdmin):
	search_fields = ['identifier']
	
	class Media:
		css = {
			"all": (settings.MEDIA_URL + "/relais.amergin/css/admin.css",)
		}
		js = (
		#	"my_code.js",
		)

### ADMIN MODELS & AND FORMS
### Bioseq form and admin model

class BioseqAnnotationAdminForm (SecondaryObjectAdminForm):
	class Meta:
		model = BioseqAnnotation
		
	def clean_name (self):
		return self.cleaned_data['name'].strip()
		
	def clean_value (self):
		return self.cleaned_data['value'].strip()

class BioseqAnnotationInline (admin.TabularInline):
	form = BioseqAnnotationAdminForm
	model = BioseqAnnotation
	extra = 0
	verbose_name = "annotation"
	verbose_name_plural = "annotations"
	
	def formfield_for_dbfield(self, db_field, **kwargs):
		# Sculpt annotation value field to smaller textarea.
		# This may seem like a good place to hide the identifier (make it a
		# HiddenWidget) but this results in an unsightly form, where the columns
		# don't match the fields below. Make it readonly (in the Django sense)
		# makes it just text, not a form field (readonly means "we just show you
		# the info). Sucessful editting of inlines needs primary key to be passed,
		# so we make it non editable by the user.
		if (db_field.attname == 'value'):
			kwargs['widget'] = widgets.Textarea(attrs={'rows': '3', 'cols': '30'})
		return super (BioseqAnnotationInline, self).formfield_for_dbfield(
			db_field,**kwargs)


class BioseqAnnotationAdmin (BaseSecondaryObjectAdmin):
	form = BioseqAnnotationAdminForm

admin.site.register (BioseqAnnotation, BioseqAnnotationAdmin)


### Bioseq qualifier form and admin model

class BioseqQualifierAdminForm (SecondaryObjectAdminForm):
	class Meta:
		model = BioseqQualifier

	def clean_name (self):
		return self.cleaned_data['name'].strip()
		
	def clean_value (self):
		return self.cleaned_data['value'].strip()
		
class BioseqQualifierInline (admin.TabularInline):
	form = BioseqQualifierAdminForm
	model = BioseqQualifier
	extra = 0
	verbose_name = "qualifier"
	verbose_name_plural = "qualifiers"

	def formfield_for_dbfield(self, db_field, **kwargs):
		if (db_field.attname == 'value'):
			kwargs['widget'] = widgets.Textarea(attrs={'rows': '3', 'cols': '30'})
		return super (BioseqQualifierInline, self).formfield_for_dbfield(
			db_field,**kwargs)
		
		
class BioseqQualifierAdmin (BaseSecondaryObjectAdmin):
	form = BioseqQualifierAdminForm

admin.site.register (BioseqQualifier, BioseqQualifierAdmin)


### Bioseq feature form and admin model

class BioseqFeatureAdminForm (SecondaryObjectAdminForm):
	class Meta:
		model = BioseqFeature
		
	def clean_location (self):
		return self.cleaned_data['location'].strip()
		
	def clean_type (self):
		return self.cleaned_data['type'].strip()

class BioseqFeatureInline (admin.TabularInline):
	form = BioseqFeatureAdminForm
	model = BioseqFeature
	extra = 0
	verbose_name = "feature"
	verbose_name_plural = "features"
	
class BioseqFeatureAdmin (BaseSecondaryObjectAdmin):
	form = BioseqFeatureAdminForm
	inlines = [
		BioseqQualifierInline,
	]
	
admin.site.register (BioseqFeature, BioseqFeatureAdmin)


### Bioseq form and admin model

class BioseqAdminForm(PrimaryObjectAdminForm):
	# We need to makea few changes to the autogenerated admin form for Bioseq:
	# - the identifier must be immutable after creation (editable for a new
	#   bioseq, readonly for all others)
	# - the identifier should be autogenerated if not supplied, and thus not
	#   required.
	
	class Meta:
		model = Bioseq

	def clean_seqdata (self):
		# normalise sequence data
		norm_seq = WHITESPACE_REGEX.sub ('', self.cleaned_data['seqdata']).lower()
		# check against sequence type
		if (self.cleaned_data['seqtype'] == 'NUCLEOTIDE'):
			alphabet = BIOSEQ_ALPHABET_NUCLEOTIDE_LETTERS
		else:
			alphabet = BIOSEQ_ALPHABET_AMINOACID_LETTERS
		alphabet = alphabet.lower()
		illegals = [(i, c) for i,c in enumerate(norm_seq) if c not in alphabet]
		# if illegal chars were found, construct & raise error
		if illegals:
			site_str = ", ".join (["%s (%s)" % (x[1], x[0]) for x in illegals])
			msg = "the sequence data contained illegal characters: %s" % site_str
			raise forms.ValidationError(msg)
		# if it's all good 
		return norm_seq
	
class BioseqAdmin (BasePrimaryObjectAdmin):
	form = BioseqAdminForm
	inlines = [
		BioseqAnnotationInline,
		BioseqFeatureInline,
	]
	radio_fields = {"seqtype": admin.HORIZONTAL}

admin.site.register (Bioseq, BioseqAdmin)


### Bioseq collection form and admin model

class BioseqCollectionMembershipInline (admin.TabularInline):
	#form = BioseqAnnotationAdminForm
	model = BioseqCollection.members.through
	extra = 0
	verbose_name = "member"
	verbose_name_plural = "members"

class BioseqCollectionAdminForm (PrimaryObjectAdminForm):

	class Meta:
		model = BioseqCollection


class BioseqCollectionAdmin (BasePrimaryObjectAdmin):
	inlines = [
		BioseqCollectionMembershipInline,
	]
	form = BioseqCollectionAdminForm

	
admin.site.register (BioseqCollection, BioseqCollectionAdmin)



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ####################################################################
