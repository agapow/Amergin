#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for routing requests to urls.

"""

### IMPORTS ###

import re

from django.conf.urls.defaults import *
from django.shortcuts import get_object_or_404, render_to_response

from relais.amergin.utils import first_not_none


### CONSTANTS & DEFINES ###

ID_TO_TITLE_RE = re.compile (r'[_\- ]+')


### IMPLEMENTATION ###

class BaseController(object):
	"""
	Mapping from urls to views for a related set of actions.
	
	In our scheme, a controller is basically a container of other controllers, represented
	as a set of urls with the same root. The controller provides the routing to
	specific actions.
	"""
	# TODO: need a way to tell contained actions about controller, e.g. pass name
	# TODO: can we turn all those ugly calls below into class properties?
	
	# identifier: unique id or name for controller, currently used for
	#	autogeneration of url and template name.
	# url: visible component in url
	# title: "SHOULD PROVIDE READABLE TITLE"
	# description = "SHOULD PROVIDE READABLE DESCRIPTION"
	
	fallback_template = "relais.amergin/base.html"
	
	def __init__ (self, identifier=None, description="", title=None,
			template=None, url=None, subcontrollers={}):
		self.identifier = identifier or self.__class__.__name__.lower()
		self.template = template or 'relais.amergin/%s.html' % self.identifier
		self.url = url or self.identifier
		self.title = title or ID_TO_TITLE_RE.sub (' ', self.identifier).capitalize()
		self.description = description
		self.subcontrollers = subcontrollers
		self.parent = None
	
	def patterns (self):
		"""
		Return a list of the urls and actions contained in this controller.
		"""
		patts = [url (u, c.view, name="%s-%s" % (self.identifier, c.identifier))
			for u, c in self.subcontrollers.iteritems()]
		patts.append (('^$', self.view))
		return patterns ('',
			*patts
		)

	def view (self, request, **kwargs):
		default = {
			'title': self.title,
			'description': self.description,
			'controller': self,
		}
		default.update (kwargs)
		return self.render (request, default)
		
	def render (self, request, dct):
		return render_to_response ([self.template, self.fallback_template],
			dct)		





		
	#@classmethod
	#def url (cls):
		#return "%s/browse/%s" % (settings.AMERGIN_URL, cls.identifier)
		
	#@classmethod
	#def index_url (cls):
		#return cls.url()

	#@classmethod
	#def create_url (cls):
		#return "%s/create" % cls.index_url()
		
	#@classmethod
	#def destroy_url (cls, id):
		#return "%s/%s/destroy" % (cls.index_url(), id)
		
	#@classmethod
	#def edit_url (cls, id):
		#return "%s/%s/edit" % (cls.index_url(), id)
		
	#@classmethod
	#def view_url (cls, id):
		#return "%s/%s/edit" % (cls.index_url(), id)
		
	#@classmethod
	#def index (cls, request):
		#found_objs = cls.model.objects.all()
		#return render_to_response('relais.amergin/base_browse_index.html', {
				#'name' : cls.model._meta.verbose_name,
				#'plural_name' : cls.model._meta.verbose_name_plural,
				#'objects': found_objs,
				#'obj_cnt': len (found_objs),
			#}
		#)
	
	#@classmethod
	#def view (cls, id=None):
	#	found_objs = cls.model.objects.all()
	#	try: 
	#		obj = cls.model.objects.get(identifier=id)
	#	except cls.model.DoesNotExist:
	#		# we have no object!  do something
	#		obj = None
	#	return render_to_response('relais.amergin/base_browse_view.html', {
	#			'name' : cls.model._meta.verbose_name,
	#			'plural_name' : cls.model._meta.verbose_name_plural,
	#			'object': obj,
	#		}
	#	)
	#	
	#@classmethod
	#def create (cls):
	#	return HttpResponse("Hello world")
	#
	#@classmethod
	#def destroy (cls, id):
	#	return HttpResponse("Hello world")
	#
	#@classmethod
	#def edit (cls, id):
	#	return HttpResponse("Hello world")
	#

