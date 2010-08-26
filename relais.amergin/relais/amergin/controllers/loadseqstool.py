#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for controllers that are tool forms.

"""

### IMPORTS ###

from toolcontroller import ToolController


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class LoadSeqsTool (ToolController):
	"""
	"""
	
	fallback_template = "relais.amergin/model.html"
	
	def __init__ (self):
		ToolController.__init__ (self,
			identifier='loadseqs',
			description="""Perform a bulk upload of biosequences from a single
				file to the repository. A collection can be formed from the
				contents.""",
			title="Load biosequences",
		)


