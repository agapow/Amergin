#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from django import forms
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response

__all__ = [
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class BaseTool (object):
	identifier = "OVERRIDE ID IN DERIVED CLASS"
	title = "OVERRIDE TITLE IN DERIVED CLASS"
	description = "OVERRIDE ID IN DERIVED CLASS"
	
	template = "tool.html"
	
	@classmethod
	def url (cls):
		return "%s/tools/%s" % (settings.AMERGIN_URL, cls.identifier)

	@classmethod
	def index (cls, request):
		results = "bar"
		form_cls = cls.ToolForm
		if request.method == 'POST': # If the form has been submitted...
			form = form_cls(request.POST) # A form bound to the POST data
			if form.is_valid(): # All validation rules pass
				# Process the data in form.cleaned_data
				results = "foo"
		else:
			form = form_cls() # An unbound form

		return render_to_response('relais.amergin/base_tool.html', {
				'identifier' : cls.identifier,
				'title' : cls.title,
				'description': cls.description,
				'form': form,
				'results': results,
			}
		)
	
	class ToolForm(forms.Form):
		username = forms.CharField(max_length=100)
		email = forms.EmailField()
		password = forms.CharField(max_length=100)



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
