#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from django.conf.urls.defaults import *
from django.http import HttpResponsePermanentRedirect

from relais.amergin.controllers.restcontroller import RestController
from relais.amergin.controllers.basecontroller import BaseController
from relais.amergin.controllers.loadseqstool import LoadSeqsTool

from relais.amergin.dev import *
import config
import models


### CONSTANTS & DEFINES ###

browse_controller = BaseController (
	identifier="browse",
	title="Browse data",
	description="Search, view and edit records.",
	template="relais.amergin/subcontroller_list.html",
	subcontrollers={
		'biosequences': RestController (models.Bioseq,
			template="relais.amergin/biosequences_index.html",
		),
		'bioseqcollections': RestController (models.BioseqCollection,
			template="relais.amergin/bioseqcollections_index.html",
		),
	}
)
 
tools_controller = BaseController (
	identifier="tools",
	description="Forms and analyses for high-level manipulation of data.",
	template="relais.amergin/subcontroller_list.html",
	subcontrollers={
		'loadseqs': LoadSeqsTool(),	
	}
)

controller_tree = BaseController (
	identifier='welcome',
	title='Welcome to Amergin',
	template='relais.amergin/subsubcontroller_list.html',
	subcontrollers={
		browse_controller.url: browse_controller,
		tools_controller.url: tools_controller,
	}
)

urlpatterns = controller_tree.urlpatterns


### IMPLEMENTATION ###	
	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################

