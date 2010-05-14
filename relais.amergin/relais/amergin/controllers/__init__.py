
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
	def show (cls, request):
		return render_to_response('relais.amergin/basebrowse.html', {
				'name' : cls.model._meta.verbose_name,
				'plural_name' : cls.model._meta.verbose_name_plural,
				'objects': cls.model.objects.all(),
			}
		)
		#return HttpResponse("Hello world")
	
	@classmethod
	def view (cls):
		return HttpResponse("Hello world")
		
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