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

class TransferTool (BaseTool):
	identifier = "transfer"
	title = "Transfer data"
	description = "Shift data from one repository to another."
	
	
register_tool (TransferTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
