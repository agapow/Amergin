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

REPOSITORY_TOOLS = [
]

INTER_TOOLS = [
]

STANDALONE_TOOLS = [
]


### IMPLEMENTATION ###

def reg_tool (reg, tool):
	assert (tool not in reg)
	reg.append (tool)


def register_repo_tool (tool):
	reg_tool (REPOSITORY_TOOLS, tool)


def register_inter_tool (tool):
	reg_tool (INTER_TOOLS, tool)


def register_standalone_tool (tool):
	reg_tool (STANDALONE_TOOLS, tool)

	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
