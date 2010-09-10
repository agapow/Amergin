#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for controllers that are tool forms.

"""

### IMPORTS ###

from basecontroller import BaseController
from django import forms
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Column

from relais.amergin import messages


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class ToolController (BaseController):
	"""
	A controller based on a model.
	
	Mainly uses the model to provide names and so forth.
	"""
	
	fallback_template = "relais.amergin/model.html"
	
	actions = [
		('search','search this site'),
	]
	fieldsets = [
		
	]
	
	def __init__ (self, identifier, title, description="", template=None):
		BaseController.__init__ (self,
			identifier=identifier,
			description=description,
			title=title or identifier,
			template=template or "relais.amergin/tool.html",
			url=identifier,
		)

	def process_form (self, data):
		# NOTE: must override this in derived class
		## Preconditions & preparation:
		msgs = []
		results = []
		## Main:
		
		## Postconditions & returns
		return msgs, results
	
	def render (self, request, dct):
		## Preconditions & preparation:
		results = msgs = None
		cls = self.__class__
		
		## Main:
		# instantiate form in one of several ways ...
		form_cls = cls.ToolForm
		# if the form has been submitted...
		if request.method == 'POST':
			form = form_cls (request.POST, request.FILES)
			# if the form is valid
			if form.is_valid():
				# get the clean data and do the work
				msgs, results = self.process_form (form.cleaned_data)
			else:
				msgs, results = (
					messages.Error ('there was a problem processing the form'),
				)
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
			helper.add_layout (Layout(*sets))
					

		# add in submit actions and a reset button
		for button in cls.actions:
			submit = Submit (button[0], button[1])
			helper.add_input (submit)
		reset = Reset ('reset','Reset form')
		helper.add_input (reset)
		
		## Postconditions & return:
		context = self.context()
		context.update ({
			'identifier' : self.identifier,
			'title' : self.title,
			'description': self.description,
			'form': form,
			'results': results,
			'msgs': msgs,
			'helper': helper,
		})
		return render_to_response ('relais.amergin/tool.html', context,
			context_instance=RequestContext(request))
	
	# NOTE: must override this in derived class
	class ToolForm (forms.Form):
		username = forms.CharField(max_length=100)
		email = forms.EmailField()
		password = forms.CharField(max_length=100)

