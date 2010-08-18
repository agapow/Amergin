
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings

class BaseAction (object):
	def __init__ (self):
		self.url = ""
		self.template = 'relais.amergin/base_browse_index.html'
		
	def __call__ (self, dct={}):
		return render_to_response (self.template, dct)

class PlaceholderAction (BaseAction):
	def __init__ (self, msg="This is a placeholder"):
		self.msg = msg
		self.url = ""
		self.template = 'relais.amergin/base_browse_index.html'
