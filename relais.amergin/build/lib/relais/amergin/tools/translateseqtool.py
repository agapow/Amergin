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

class TranslateSeqTool (RepoTool):
	identifier = "transseq"
	title = "Translate sequences"
	description = "Shift biosequences from one file format to another."
	
	
register_standalone_tool (TranslateSeqTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
