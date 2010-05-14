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

class LoadSeqsTool (RepoTool):
	identifier = "loadseq"
	title = "Load biosequences"
	description = "Perform a bulk upload of biosequences (and sequence collections) to the repository."
	
	
register_repo_tool (LoadSeqsTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
