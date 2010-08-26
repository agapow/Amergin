#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION

"""


### IMPORTS ###

from django import template
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model


## CONSTANTS & DEFINES ###

register = template.Library()


### IMPLEMENTATION ###

@register.filter
def adminurl (obj_or_model):
	content_type = ContentType.objects.get_for_model (obj_or_model)
	return "/admin/amergin/%s" % content_type.model


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ####################################################################

