#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for controllers based on models.

"""

### IMPORTS ###

import re

from django.views.generic import list_detail
from django.template.loader import select_template
from django.http import HttpResponsePermanentRedirect
from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from relais.amergin.utils import (is_sequence, is_callable, is_string)

from basecontroller import BaseController


### CONSTANTS & DEFINES ###

NAME_TO_ID_RE = re.compile ('\s+')


### IMPLEMENTATION ###

class ModelController (BaseController):
	"""
	A controller based on a model.
	
	Mainly uses the model to provide names and so forth.
	"""
	
	fallback_template = "relais.amergin/model.html"
	
	def __init__ (self, model, identifier=None, description="", title=None,
			template=None, url=None, subcontrollers={}):
		self.model = model
		self.name = self.model._meta.verbose_name
		self.name_plural = self.model._meta.verbose_name_plural
		BaseController.__init__ (self,
			identifier = identifier or NAME_TO_ID_RE.sub ('', self.name_plural),
			description=description,
			title= title or self.name_plural,
			template=template or "relais.amergin/model.html",
			url=url,
			subcontrollers=subcontrollers,
		)
		
	def context (self):
		context = BaseController.context (self)
		context.update ({
			'model': self.model,
		})
		return context
		
	def render (self, request, dct):
		"""
		Given a request and mapping of variables, render and return appropriately.
		"""
		# TODO: pagination
		# TODO: filter
		query_set = self.model.objects.all()
		dct.update ({
			'obj_cnt': query_set.count(),			
		})
		# include RequestConext by default
		return list_detail.object_list (
			request,
			queryset = self.model.objects.all(),
			template_name = self.template,
			#template_object_name = "books",
			extra_context = dct,
		)

