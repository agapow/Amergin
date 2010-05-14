#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION

"""

### IMPORTS ###

from models import Repository
from django.contrib import admin
from amergin.polls.models import Choice


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


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ####################################################################

