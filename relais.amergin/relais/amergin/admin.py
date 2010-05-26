#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION

"""

### IMPORTS ###

from models import *
from django.contrib import admin
from django.forms import widgets
from django import forms


#from amergin.polls.models import Choice


## CONSTANTS & DEFINES ###

## IMLEMENTATION ###

#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3
#
#class PollAdmin(admin.ModelAdmin):
#	list_display = ('question', 'pub_date', 'was_published_today')
#	inlines = [ChoiceInline]
#	search_fields = ['question', 'pub_date']
#	date_hierarchy = 'pub_date'

#admin.site.register(Poll, PollAdmin)

class BioseqAnnotationAdminForm(forms.ModelForm):
	class Meta:
		model = BioseqAnnotation

class BioseqAnnotationInline (admin.TabularInline):
	form = BioseqAnnotationAdminForm
	model = BioseqAnnotation
	extra = 0
	verbose_name = "annotation"
	verbose_name_plural = "annotations"
	readonly_fields = [
		'identifier',
	]
	
	def formfield_for_dbfield(self, db_field, **kwargs):
		# sculpt annotation value field to smaller textarea
		if (db_field.attname == 'value'):
			kwargs['widget'] = widgets.Textarea(attrs={'rows': '3', 'cols': '50'})
		# sucessful editting of inlines needs primary key to be passed,
		# but don't want to show it
		#elif (db_field.attname == 'identifier'):
		#	kwargs['widget'] = widgets.HiddenInput
		return super (BioseqAnnotationInline, self).formfield_for_dbfield(
			db_field,**kwargs)


class BseqAdminForm(forms.ModelForm):
	class Meta:
		model = Bioseq
		
class BioseqAdmin (admin.ModelAdmin):
	form = BseqAdminForm
	inlines = [
		BioseqAnnotationInline,
	]
	radio_fields = {"seqtype": admin.HORIZONTAL}
	search_fields = ['identifier', 'title', 'description']

admin.site.register (Bioseq, BioseqAdmin)


class BioseqAnnotationAdmin (admin.ModelAdmin):
	pass

admin.site.register (BioseqAnnotation, BioseqAnnotationAdmin)

class BioseqCollectionAdmin (admin.ModelAdmin):
	pass

admin.site.register (BioseqCollection, BioseqCollectionAdmin)

class BioseqCollectionsBioseqAdmin (admin.ModelAdmin):
	pass

admin.site.register (BioseqCollectionsBioseq, BioseqCollectionsBioseqAdmin)

class BioseqExtrefAdmin (admin.ModelAdmin):
	pass

admin.site.register (BioseqExtref, BioseqExtrefAdmin)

class BioseqFeatureAdmin (admin.ModelAdmin):
	pass

admin.site.register (BioseqFeature, BioseqFeatureAdmin)

class BioseqQualifierAdmin (admin.ModelAdmin):
	pass

admin.site.register (BioseqQualifier, BioseqQualifierAdmin)




	

### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ####################################################################

