#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for welcome / front page controllers.

"""

### IMPORTS ###

from basecontroller import BaseController


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class WelcomeController (BaseController):
	"""
	A controller based on a model.
	
	Mainly uses the model to provide names and so forth.
	"""
	# TODO: need a way to tell contained actions about controller, e.g. pass name
	# TODO: can we turn all those ugly calls below into class properties?
	
	# identifier: unique id or name for controller, currently used for
	#	autogeneration of url and template name.
	# url: visible component in url
	# title: "SHOULD PROVIDE READABLE TITLE"
	# description = "SHOULD PROVIDE READABLE DESCRIPTION"
	
	fallback_template = "relais.amergin/welcome.html"
	
	def __init__ (self, identifier="welcome", description="", title=None,
			template=None, url=None, subcontrollers={}):
		BaseController.__init__ (self,
			identifier = identifier,
			description=description,
			title=title,
			template=template,
			url=url,
			subcontrollers=subcontrollers,
		)

	def view (self, request):
		return BaseController.view (self, request,
			subcontrollers=self.subcontrollers)

	

