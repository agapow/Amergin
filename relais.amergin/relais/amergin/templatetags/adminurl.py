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
from django.core.urlresolvers import reverse
from django.contrib.admin.util import quote
from django.utils.safestring import mark_safe

## CONSTANTS & DEFINES ###

register = template.Library()


### IMPLEMENTATION ###

@register.filter
def adminurl (obj_or_model):
	content_type = ContentType.objects.get_for_model (obj_or_model)
	return "/admin/amergin/%s" % content_type.model

@register.filter
def admin_edit_url (object):
	return "/admin/%s/%s/%s/" % (
		object._meta.app_label,
		object._meta.module_name,
		quote (object.identifier),
	)
	
@register.filter
def admin_delete_url (object):
	return "%sdelete/" % admin_edit_url (object)
	
@register.filter
def admin_create_url (model):
	return "/admin/%s/%s/add/" % (
		model._meta.app_label,
		model._meta.module_name,
	)

@register.filter
def admin_edit_url2 (obj):
	return mark_safe(u"%s" % quote(obj.identifier))



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ####################################################################

