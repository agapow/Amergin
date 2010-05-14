from django.conf.urls.defaults import *
from piston.resource import Resource
from relais.amergin.rest import handlers

pats = ['']
rsrc = [
	[BioseqHandler, 'bioseqs'],
]


bioseq_handler = Resource(BioseqHandler)

urlpatterns = patterns('',
   url(r'^bioseqs/(?P<id>.+)$', bioseq_handler),
   url(r'^bioseqs$', bioseq_handler),
)