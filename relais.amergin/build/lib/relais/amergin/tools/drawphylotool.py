#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from basetool import RepoTool
from registry import register_standalone_tool

__all__ = [
]

### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class DrawPhyloTool (RepoTool):
	identifier = "drawphylo"
	title = "Draw phylogeny"
	description = "Draw a phylogeny from a Newick representation."
	
	
register_standalone_tool (DrawPhyloTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
