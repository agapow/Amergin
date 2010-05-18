
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings

from relais.amergin import models
from registry import register_controller

class BaseController(object):
	model = None
	identifier = "OVERRIDE THIS IDENTIFIER"
	title = "OVERRIDE THIS TITLE"
	description = "OVERRIDE THIS DESCRIPTION"
	
	@classmethod
	def url (cls):
		return "%s/browse/%s" % (settings.AMERGIN_URL, cls.identifier)
		
	@classmethod
	def index_url (cls):
		return cls.url()

	@classmethod
	def create_url (cls):
		return "%s/create" % cls.index_url()
		
	@classmethod
	def destroy_url (cls, id):
		return "%s/%s/destroy" % (cls.index_url(), id)
		
	@classmethod
	def edit_url (cls, id):
		return "%s/%s/edit" % (cls.index_url(), id)
		
	@classmethod
	def view_url (cls, id):
		return "%s/%s/edit" % (cls.index_url(), id)
		
	@classmethod
	def index (cls, request):
		found_objs = cls.model.objects.all()
		return render_to_response('relais.amergin/base_browse_index.html', {
				'name' : cls.model._meta.verbose_name,
				'plural_name' : cls.model._meta.verbose_name_plural,
				'objects': found_objs,
				'obj_cnt': len (found_objs),
			}
		)
	
	@classmethod
	def view (cls, id=None):
		found_objs = cls.model.objects.all()
		try: 
			obj = cls.model.objects.get(identifier=id)
		except cls.model.DoesNotExist:
			# we have no object!  do something
			obj = None
		return render_to_response('relais.amergin/base_browse_view.html', {
				'name' : cls.model._meta.verbose_name,
				'plural_name' : cls.model._meta.verbose_name_plural,
				'object': obj,
			}
		)
		
	@classmethod
	def create (cls):
		return HttpResponse("Hello world")
	
	@classmethod
	def destroy (cls, id):
		return HttpResponse("Hello world")
	
	@classmethod
	def edit (cls, id):
		return HttpResponse("Hello world")
	

class BioseqController(BaseController):
	model = models.Bioseq
	identifier = "bioseqs"
	title = "Biosequences"
	description = "Molecular sequences derived from isolates."
	
register_controller(BioseqController)