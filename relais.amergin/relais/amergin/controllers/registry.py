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

def register_controller (controller):
	global registry
	assert (controller not in registry)
	registry.append (controller)

	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
