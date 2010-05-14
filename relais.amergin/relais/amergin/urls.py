#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from django.conf.urls.defaults import *

import models
from relais.amergin.controllers.registry import registry as controller_registry
from relais.amergin.tools.registry import registry as tool_registry

import config


### CONSTANTS & DEFINES ###

add_urls = []
for c in controller_registry:
	 add_urls.append ((r'^browse/%s$' % c.identifier, c.show))
	 add_urls.append ((r'^browse/%s/create$' % c.identifier, c.create))
	 add_urls.append ((r'^browse/%s/edit$' % c.identifier, c.edit))
	 add_urls.append ((r'^browse/%s/(?P<id>[^/]+)/destroy$' % c.identifier, c.destroy))
	 add_urls.append ((r'^browse/%s/(?P<id>[^/]+)$' % c.identifier, c.view))

for t in tool_registry:
	 add_urls.append ((r'^tools/%s$' % t.identifier, t.show))
print add_urls

urlpatterns = patterns('',
	 
	# top level opening page
	(r'^$', 'relais.amergin.views.welcome'),
	
	*add_urls
	#
	#(r'^browse/', include(rest.urls)),
	
#	# inter repo tools
#	(r'^%s$' % config.INTER_TOOLS_DIR, 'relais.amergin.views.list_inter_tools'),
#	# solo tools
#	(r'^%s$' % config.STANDALONE_TOOLS_DIR, 'relais.amergin.views.list_standalone_tools'),
#	# all repositories top level
#	(r'^%s$' % config.ALL_REPOS_DIR, 'relais.amergin.views.list_repos'),
#	# individual repo top level
#	(r'^%s/(?P<repo_id>[^/]+)$' % config.ALL_REPOS_DIR, 'relais.amergin.views.repo_contents'),
#	# individual repo bioseqs
#	(r'^%s/(?P<repo_id>[^/]+)/%s$' % (config.ALL_REPOS_DIR, config.BSEQ_DATA_DIR),
#		'relais.amergin.views.list_bioseqs'),
#	(r'^%s/(?P<repo_id>[^/]+)/%s/%s$' % (config.ALL_REPOS_DIR, 'tools', 'analyseseq'),
#		'relais.amergin.views.analyseseq'),

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

