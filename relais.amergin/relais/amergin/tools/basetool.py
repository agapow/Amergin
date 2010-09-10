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

from relais.amergin import messages

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

	# Return visualised output and messages as result of form processing
	#
	@classmethod
	def process_form (cls, data):
		## Preconditions & preparation:
		msgs = results = []
		## Main:
		
		## Postconditions & returns
		return msgs, results
	
	@classmethod
	def index (cls, request):
		## Preconditions & preparation:
		results = msgs = None
		
		## Main:
		# instantiate form in one of several ways ...
		form_cls = cls.ToolForm
		# if the form has been submitted...
		if request.method == 'POST':
			form = form_cls(request.POST, request.FILES)
			# if the form is valid
			if form.is_valid():
				# get the clean data and do the work
				msgs, results = cls.process_form (form.cleaned_data)
			else:
				msgs = [messages.Error ("there was problem processing the form")]
		else:
			# if you're coming to the form anew, make an unbound form
			form = form_cls()

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
			helper.add_layout (Layout (*sets))

		# add in submit actions and a reset button
		for button in cls.actions:
			submit = Submit (button[0], button[1].title())
			helper.add_input (submit)
		reset = Reset ('reset','Reset form')
		helper.add_input (reset)
		
		## Postconditions & return:
		return render_to_response('relais.amergin/base_tool.html', {
				'identifier' : cls.identifier,
				'title' : cls.title,
				'description': cls.description,
				'form': form,
				'results': results,
				'messages': msgs,
				'helper': helper,
			}
		)
	
	class ToolForm (forms.Form):
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
