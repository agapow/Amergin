#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for controllers based on models.

"""

### IMPORTS ###

from basecontroller import BaseController


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class ModelController (BaseController):
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
	
	fallback_template = "relais.amergin/model.html"
	
	def __init__ (self, model, identifier=None, description="", title=None,
			template=None, url=None, subcontrollers={}):
		self.model = model
		self.name = self.model._meta.verbose_name
		self.name_plural = self.model._meta.verbose_name_plural
		BaseController.__init__ (self,
			identifier = identifier or self.name_plural,
			description=description,
			title=title,
			template=template,
			url=url,
			subcontrollers=subcontrollers,
		)

	def view (self, request, **kwargs):
		# retrieve all objects
		retrieved_objs = self.model.objects.all()
		return BaseController.view (self, request,
			model=self.model,
			objs=retrieved_objs,
		   obj_cnt=len (retrieved_objs),
		)
		
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
		
	##@classmethod
	##def index (cls, request):
	##	found_objs = cls.model.objects.all()
	##	return render_to_response('relais.amergin/base_browse_index.html', {
	##			'name' : cls.model._meta.verbose_name,
	##			'plural_name' : cls.model._meta.verbose_name_plural,
	##			'objects': found_objs,
	##			'obj_cnt': len (found_objs),
	##		}
	##	)
	
	##@classmethod
	##def view (cls, id=None):
	##	found_objs = cls.model.objects.all()
	##	try: 
	##		obj = cls.model.objects.get(identifier=id)
	##	except cls.model.DoesNotExist:
	##		# we have no object!  do something
	##		obj = None
	##	return render_to_response('relais.amergin/base_browse_view.html', {
	##			'name' : cls.model._meta.verbose_name,
	##			'plural_name' : cls.model._meta.verbose_name_plural,
	##			'object': obj,
	##		}
	##	)
		
	#@classmethod
	#def create (cls):
		#return HttpResponse("Hello world")
	
	#@classmethod
	#def destroy (cls, id):
		#return HttpResponse("Hello world")
	
	#@classmethod
	#def edit (cls, id):
		#return HttpResponse("Hello world")
	

