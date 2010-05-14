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

registry = [
]

### IMPLEMENTATION ###

def register_tool (tool):
	global registry
	assert (tool not in registry)
	registry.append (tool)

	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
