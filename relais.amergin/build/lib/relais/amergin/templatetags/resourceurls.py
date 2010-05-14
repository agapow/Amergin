#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION

"""


### IMPORTS ###

import os

from django import template
from django.template import loader, Node, Variable
from django.utils.encoding import smart_str, smart_unicode
from django.template.defaulttags import url
from django.template import VariableDoesNotExist


## CONSTANTS & DEFINES ###

register = template.Library()


### IMPLEMENTATION ###

def url_join (*args):
	"""Join any arbitrary strings into a forward-slash delimited list.
	Do not strip leading / from first element, nor trailing / from last element."""
	if len(args) == 0:
		return ""

	if len(args) == 1:
		return str(args[0])

	else:
		args = [str(arg).replace("\\", "/") for arg in args]

		work = [args[0]]
		for arg in args[1:]:
			if arg.startswith("/"):
				work.append(arg[1:])
			else:
				work.append(arg)

		joined = reduce(os.path.join, work)

	return joined.replace("\\", "/")


@register.tag
def resource_url (parser, token):
	return AppResourceUrlNode (token.split_contents()[1:])


class AppResourceUrlNode (Node):
	def __init__(self, vars):
		"""
		First var is title, second var is url context variable
		"""
		self.vars = map (Variable, vars)

	def render(self, context):
		res_url = self.vars[0].var
		return url_join ('/site_media', res_url)


@register.tag
def include_stylesheet (parser, token):
	return InclStylesheetNode (token.split_contents()[1:])


class InclStylesheetNode (Node):
	def __init__(self, vars):
		"""
		First var is title, second var is url context variable
		"""
		self.vars = map (Variable, vars)

	def render (self, context):
		tmpl = """<LINK href="%s" rel="stylesheet" type="text/css">"""
		res_url = self.vars[0].var
		return tmpl % url_join ('/site_media', res_url)	



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ####################################################################

