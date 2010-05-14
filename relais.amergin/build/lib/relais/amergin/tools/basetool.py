#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

__all__ = [
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class BaseTool (object):
	identifier = "OVERRIDE ID IN DERIVED CLASS"
	title = "OVERRIDE TITLE IN DERIVED CLASS"
	description = "OVERRIDE ID IN DERIVED CLASS"
	
	
class RepoTool (BaseTool):
	pass


class InterRepoTool (BaseTool):
	pass


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
