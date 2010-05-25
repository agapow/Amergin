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

class BioseqAnnotationInline (admin.TabularInline):
	model = BioseqAnnotation
	extra = 1
	verbose_name = "annotation"
	verbose_name_plural = "annotations"

class BioseqAdmin (admin.ModelAdmin):
	inlines = [
		BioseqAnnotationInline,
	]

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

