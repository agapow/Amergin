#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from basetool import InterRepoTool
from registry import register_inter_tool

__all__ = [
]

### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class CompareTool (InterRepoTool):
	identifier = "compare"
	title = "Compare repositories"
	description = "Check for shared or unique data across."
	
	
register_inter_tool (CompareTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
