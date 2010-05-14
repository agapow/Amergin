#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Small utility functions for use throughout Amergin.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

#__all__ = [
#	'TagAttrib',
#]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###	

def idsrc_to_str (ident, src=None):
	"""
	Package an ID and source designator into a single string.
	
	The combined ID and source are expressed as "com.example.foo:XYZ123".
	
	"""
	if (src):
		return u'%s:%s' % (src, ident)
	else:
		return unicode (ident)


def str_to_idsrc (s):
	"""
	Unpack an ID and source designator from a string.
	
	:Returns:
		A tuple of (ID, source). Note the the order is the same as the order
		for construction.
	
	"""
	splits = s.split (':', 1)
	if (len (splits) == 2):
		return splits[1], splits[0]
	else:
		return splits[0]



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
