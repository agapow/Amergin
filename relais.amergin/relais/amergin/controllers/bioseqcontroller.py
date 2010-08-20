#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Controller for biosequence actions.

"""

### IMPORTS ###

from modelcontroller import ModelController
from relais.amergin import models


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class BioseqController (ModelController):
	"""
	"""
	def __init__ (self):
		ModelController.__init__ (self, models.Bioseq,
			description="Molecular sequences derived from isolates.",							  
		)
