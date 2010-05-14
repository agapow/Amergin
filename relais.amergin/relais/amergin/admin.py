#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION

"""

### IMPORTS ###

from models import *
from django.contrib import admin
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

class RepoAdmin (admin.ModelAdmin):
	list_display = ('identifier', 'title')

admin.site.register (Repository, RepoAdmin)

class AssayAdmin (admin.ModelAdmin):
	pass

admin.site.register (Assay, AssayAdmin)

class BioseqannotationAdmin (admin.ModelAdmin):
	pass

admin.site.register (Bioseqannotation, BioseqannotationAdmin)

class BioseqcollectionAdmin (admin.ModelAdmin):
	pass

admin.site.register (Bioseqcollection, BioseqcollectionAdmin)

class BioseqcollectionsBioseqAdmin (admin.ModelAdmin):
	pass

admin.site.register (BioseqcollectionsBioseq, BioseqcollectionsBioseqAdmin)

class BioseqextrefAdmin (admin.ModelAdmin):
	pass

admin.site.register (Bioseqextref, BioseqextrefAdmin)

class BioseqfeatureAdmin (admin.ModelAdmin):
	pass

admin.site.register (Bioseqfeature, BioseqfeatureAdmin)

class BioseqqualifierAdmin (admin.ModelAdmin):
	pass

admin.site.register (Bioseqqualifier, BioseqqualifierAdmin)

class BioseqAdmin (admin.ModelAdmin):
	pass

admin.site.register (Bioseq, BioseqAdmin)

class DocumentAdmin (admin.ModelAdmin):
	pass

admin.site.register (Document, DocumentAdmin)

class RegionAdmin (admin.ModelAdmin):
	pass

admin.site.register (Region, RegionAdmin)

class SampleAdmin (admin.ModelAdmin):
	pass

admin.site.register (Sample, SampleAdmin)
	

### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ####################################################################

