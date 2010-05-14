#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from basetool import RepoTool
from registry import register_repo_tool

__all__ = [
]

### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class LoadDocsTool (RepoTool):
	identifier = "OVERRIDE ID IN DERIVED CLASS"
	title = "OVERRIDE TITLE IN DERIVED CLASS"
	description = "OVERRIDE ID IN DERIVED CLASS"
	
	
register_repo_tool (LoadDocsTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
