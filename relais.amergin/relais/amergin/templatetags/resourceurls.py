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

from django.conf import settings


## CONSTANTS & DEFINES ###

register = template.Library()


### IMPLEMENTATION ###

def url_join (*args):
	"""Join any arbitrary strings into a forward-slash delimited list.
	Do not strip leading / from first element, nor trailing / from last element."""
	if len(args) == 0:
		return ""
	elif len(args) == 1:
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
		return url_join (settings.MEDIA_URL, res_url)


### INCLUDE STYLESHEET LINK

@register.tag
def include_css (parser, token):
	return InclCssNode (token.split_contents()[1:])

class InclCssNode (Node):
	def __init__(self, vars):
		"""
		First var is title, second var is url context variable
		"""
		self.vars = map (Variable, vars)

	def render (self, context):
		tmpl = """<link href="%s" rel="stylesheet" type="text/css" />"""
		res_url = self.vars[0].var
		return tmpl % url_join (settings.MEDIA_URL, 'relais.amergin', 'css', res_url)	


### INCLUDE JAVASCRIPT 

@register.tag
def include_js (parser, token):
	return InclJsNode (token.split_contents()[1:])

class InclJsNode (Node):
	def __init__(self, vars):
		"""
		First var is title, second var is url context variable
		"""
		self.vars = map (Variable, vars)

	def render (self, context):
		tmpl = """<SCRIPT src="%s" type="text/javascript"></SCRIPT>"""
		res_url = self.vars[0].var
		return tmpl % url_join (settings.MEDIA_URL, 'relais.amergin', res_url)
		

### INTERNAL LINKS
# urls relative to top of application
# TODO: this works but requires AMERGIN_URL in the settings file. Bad.

@register.tag
def internal_link (parser, token):
	try:
		tag_name, address, content = token.contents.split()
		print token.contents.split()
	except ValueError:
		raise template.TemplateSyntaxError, \
			"%r tag requires exactly two arguments" % token.contents.split()[0]
	if (content[0] == content[-1] and content[0] in ('"', "'")):
		content = content[1:-1]
	return InternalLinkNode (address, content)

class InternalLinkNode (Node):
	def __init__(self, address, content):
		"""
		First var is title, second var is url context variable
		"""
		self.address = address
		self.content = content

	def render (self, context):
		return """<A HREF="%s">%s</A>""" % (
			url_join (settings.AMERGIN_URL, self.address),
			self.content,
		)
		

### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ####################################################################

