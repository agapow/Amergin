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

class CompareTool (BaseTool):
	identifier = "compare"
	title = "Compare repositories"
	description = "Check for shared or unique data across."
	
	
register_tool (CompareTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
