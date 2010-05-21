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

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Column

__all__ = [
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class BaseTool (object):
	identifier = "OVERRIDE ID IN DERIVED CLASS"
	title = "OVERRIDE TITLE IN DERIVED CLASS"
	description = "OVERRIDE ID IN DERIVED CLASS"
	actions = [
		('search','search this site'),
	]
	fieldsets = [
		
	]
	
	template = "tool.html"
	
	@classmethod
	def url (cls):
		return "%s/tools/%s" % (settings.AMERGIN_URL, cls.identifier)

	@classmethod
	def process_form (cls, data):
		## Errors
		## Postconditions & returns
		return data, None
	
	@classmethod
	def index (cls, request):
		results = msgs = None
		
		form_cls = cls.ToolForm
		if request.method == 'POST': # If the form has been submitted...
			form = form_cls(request.POST) # A form bound to the POST data
			if form.is_valid(): # All validation rules pass
				# Process the data in form.cleaned_data
				# TODO: actually do the form work
				results, msgs = cls.process_form (form.cleaned_data)
				print form.cleaned_data
			else:
				msgs = (
					('error', 'there was problem processing the form'),
				)
		else:
			form = form_cls() # An unbound form

		helper = FormHelper()
		
		# Add in a class and id
		helper.form_id = 'this-form-rocks'
		helper.form_class = 'tool_form'
		
		# if necessary, do fieldsets
		if cls.fieldsets:
			sets = []
			for field_pair in cls.fieldsets:
				if (isinstance (field_pair, basestring)):
					# if just a naked field name
					field_pair = ['', field_pair]
				sets.append (Fieldset (*field_pair))
			helper.add_layout (Layout(*sets))
					

		# add in submit actions and a reset button
		for button in cls.actions:
			submit = Submit (button[0], button[1])
			helper.add_input (submit)
		reset = Reset ('reset','reset button')
		helper.add_input (reset)
		
		return render_to_response('relais.amergin/base_tool.html', {
				'identifier' : cls.identifier,
				'title' : cls.title,
				'description': cls.description,
				'form': form,
				'results': results,
				'errors': msgs,
				'helper': helper,
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
