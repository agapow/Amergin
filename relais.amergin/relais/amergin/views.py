#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from relais.amergin import models

from relais.amergin.controllers.registry import registry as controller_registry
from relais.amergin.tools.registry import registry as tool_registry

__all__ = [
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def welcome (request):
	info_dict = {
		'isolate_cnt': len(models.Sample.objects.all()),
		'bioseq_cnt': len(models.Bioseq.objects.all()),
		'bioseqcollection_cnt': len(models.BioseqCollection.objects.all()),
		'controller_list': controller_registry,
		'tool_list': tool_registry,
	}
	return render_to_response ('relais.amergin/welcome.html',
		info_dict,
		context_instance = RequestContext(request)
	)
	return render_to_response ('relais.amergin/welcome.html',
		info_dict,
		context_instance = RequestContext(request)
	)
	
def analyseseq	(request, repo_id):
	return render_to_response ('relais.amergin/analyseseqtool.html',
		{
			'pagename': 'list_inter_tools',
		},
	)


def list_inter_tools (request):
	return render_to_response ('relais.amergin/test.html',
		{
			'pagename': 'list_inter_tools',
		},
	)


def list_standalone_tools (request):
	return render_to_response ('relais.amergin/test.html',
		{
			'pagename': 'list_standalone_tools',
		},
	)
	
	
def list_repos (request):
	return render_to_response ('relais.amergin/test.html',
		{
			'pagename': 'list_repos',
		},
	)


def repo_contents (request, repo_id):
	return render_to_response ('relais.amergin/test.html',
		{
			'pagename': 'repo_contents',
		},
	)


def list_bioseqs (request, repo_id):
	return render_to_response ('relais.amergin/browsedata.html',
		{
			'pagename': 'Browse biosequences',
		},
	)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################


