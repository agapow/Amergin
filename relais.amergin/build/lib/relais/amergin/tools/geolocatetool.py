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

class GeoLocateTool (RepoTool):
	identifier = "geolocate"
	title = "Geo-lookup"
	description = "Lookup and check geolocations."
	
	
register_standalone_tool (GeoLocateTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
