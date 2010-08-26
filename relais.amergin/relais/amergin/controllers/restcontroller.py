#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for model controllers with a rest interface

"""

### IMPORTS ###

from django.conf.urls.defaults import *
from django.shortcuts import get_object_or_404, render_to_response

from modelcontroller import ModelController
from relais.amergin.dev import *
from relais.amergin import messages


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class RestController (ModelController):
	"""
	A model controller with a rest interface.
	"""
	
	def __init__ (self, model, identifier=None, description="", title=None,
		template=None, url=None, subcontrollers={}):
		ModelController.__init__ (self,
			model=model,
			identifier=identifier,
			description=description,
			title=title,
			template=template or "relais.amergin/rest.html",
			url=url,
			subcontrollers=subcontrollers,
		)
		self.template_show = "relais.amergin/rest_show_%s.html" % self.identifier
		
	def patterns (self):
		"""
		Return a list of the urls and actions contained in this controller.
		"""
		patts = [
			# create
			url (r'^create$', self.create, name="%s-create" % self.identifier),
			# view
			url (r'^(?P<id>[^/]+)$', self.show, name="%s-show" % self.identifier),
			# delete
			url (r'^(?P<id>[^/]+)/delete$', self.delete, name="%s-delete" % self.identifier),
			# edit
			url (r'^(?P<id>[^/]+)/edit$', self.edit, name="%s-edit" % self.identifier),
			# index
			url ('^$', self.view, name=self.identifier),
		]
		## Return:
		pp ("I'm here")
		pp (patts)
		return patterns ('', *patts)
	
	urlpatterns = property (patterns)
	
	def create (self, request):
		context = self.context()
		pass
		
	def show (self, request, id=None):
		context = self.context()

		try:
			obj = self.model.objects.get (identifier=id)
		except:
			obj = None
			context['msgs'].append (messages.Error ("""Can't find %s:
				either it does not exist or you do not have permission to access
				it.""" % self.name))
		context.update({
			'title': '%s %s' % (self.name, id),
			'obj': obj,
			'description': None,
		})
		pp (self.template_show)
		return render_to_response ([self.template_show, 'relais.amergin/rest_show.html'],
			context)
		
	def delete (self, request, id):
		pass
		
	
	def edit (self, request, id):
		pass
		
	
