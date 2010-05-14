#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from basetool import BaseTool
from registry import register_tool

__all__ = [
]

### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class AnalyseSeqTool (BaseTool):
	identifier = "OVERRIDE ID IN DERIVED CLASS"
	title = "OVERRIDE TITLE IN DERIVED CLASS"
	description = "OVERRIDE ID IN DERIVED CLASS"
	
	
register_tool (AnalyseSeqTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
