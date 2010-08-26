#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for routing requests to urls.

"""

### IMPORTS ###

import re

from django.conf.urls.defaults import *
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponsePermanentRedirect

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
		self.subcontrollers = {}
		for k, v in subcontrollers.iteritems():
			self.add_subcontroller (k, v)
		self.parent = None
	
	def add_subcontroller (self, url, sc):
		sc.url = url
		sc.parent = self
		self.subcontrollers[url] = sc
		
	def patterns (self):
		"""Return the urlpatterns of all that within this controller."""
		patts = []
		for u, c in self.subcontrollers.iteritems():
			patts.append ((r'^%s/' % u,
				include (c)))
			patts.append ((r'^%s$' % u,
				lambda request: HttpResponsePermanentRedirect (r'%s/' % u)))
		patts.append (url ('^$', self.view, name=self.identifier))
		return patterns ('', *patts)
		
	urlpatterns = property (patterns)

	def view (self, request, **kwargs):
		"""Return default rendering/view."""
		context = self.context()
		context.update (kwargs)
		return self.render (request, context)
		
	def render (self, request, dct):
		"""
		Given a request and mapping of variables, render and return appropriately.
		"""
		return render_to_response ([self.template, self.fallback_template],
			dct)		
		
	def context (self):
		"""Return values to be included in template."""	
		return {
			'title': self.title,
			'description': self.description,
			'controller': self,
			'msgs': [],
		}
