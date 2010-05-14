#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from django.conf.urls.defaults import *
from relais.amergin.models import Repository

import config


### CONSTANTS & DEFINES ###


info_dict = {
    'repo_query': Repository.objects.all(),
}

urlpatterns = patterns('',
	# test page for template
	(r'^test$', 'relais.amergin.views.test'),
	# top level opening page
	(r'^$', 'relais.amergin.views.welcome', info_dict),
	# inter repo tools
	(r'^%s$' % config.INTER_TOOLS_DIR, 'relais.amergin.views.list_inter_tools'),
	# solo tools
	(r'^%s$' % config.STANDALONE_TOOLS_DIR, 'relais.amergin.views.list_standalone_tools'),
	# all repositories top level
	(r'^%s$' % config.ALL_REPOS_DIR, 'relais.amergin.views.list_repos'),
	# individual repo top level
	(r'^%s/(?P<repo_id>[^/]+)$' % config.ALL_REPOS_DIR, 'relais.amergin.views.repo_contents'),
	# individual repo bioseqs
	(r'^%s/(?P<repo_id>[^/]+)/%s$' % (config.ALL_REPOS_DIR, config.BSEQ_DATA_DIR),
		'relais.amergin.views.list_bioseqs'),
	(r'^%s/(?P<repo_id>[^/]+)/%s/%s$' % (config.ALL_REPOS_DIR, 'tools', 'analyseseq'),
		'relais.amergin.views.analyseseq'),
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

