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
from relais.amergin.controllers.welcomecontroller import WelcomeController
from relais.amergin.controllers.modelcontroller import ModelController

import config


### CONSTANTS & DEFINES ###

model_controllers = [
	ModelController (models.Bioseq),
]

controller_tree = WelcomeController (
	subcontrollers = dict ([(m.url, m) for m in model_controllers])
)
 

urlpatterns = controller_tree.patterns()
#
#   (r'^foo$', include (controller_tree.patterns())),
#
#	# redirect "browse" and "tools" directory to welcome page
#	#(r'^browse$', lambda request: HttpResponsePermanentRedirect(r'/')),
#	#(r'^tools$', lambda request: HttpResponsePermanentRedirect(r'/')),
#)


### IMPLEMENTATION ###	
	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################

