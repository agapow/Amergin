#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from django.conf.urls.defaults import *
from django.http import HttpResponsePermanentRedirect

import models
from relais.amergin.controllers.registry import registry as controller_registry
from relais.amergin.tools.registry import registry as tool_registry

import config


### CONSTANTS & DEFINES ###

add_urls = []
#for c in controller_registry:
#	add_urls.append ((r'^browse/%s$' % c.identifier, c.index))
#	add_urls.append ((r'^browse/%s/create$' % c.identifier, c.create))
#	add_urls.append ((r'^browse/%s/edit$' % c.identifier, c.edit))
#	add_urls.append ((r'^browse/%s/(?P<id>[^/]+)/destroy$' % c.identifier, c.destroy))
#	add_urls.append ((r'^browse/%s/(?P<id>[^/]+)$' % c.identifier, c.view))

for c in controller_registry:
	for url, action in c.get_views():
		add_urls.append ((r'^browse/%s$' % url, action))

for t in tool_registry:
	add_urls.append ((r'^tools/%s$' % t.identifier, t.index))

urlpatterns = patterns('',
	
	# top level opening page
	(r'^$', 'relais.amergin.views.welcome'),
	
	# redirect "browse" and "tools" directory to welcome page
	(r'^browse$', lambda request: HttpResponsePermanentRedirect(r'/')),
	(r'^tools$', lambda request: HttpResponsePermanentRedirect(r'/')),
	
	*add_urls
)


### IMPLEMENTATION ###	
	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################

