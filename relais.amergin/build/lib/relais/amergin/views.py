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
from amergin.polls.models import Choice, Poll

from relais.amergin.tools.registry import INTER_TOOLS, STANDALONE_TOOLS

__all__ = [
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def test (request):
	return render_to_response ('relais.amergin/test.html',
		{
			'repos': now,
			'inter_tools': INTERREPO_TOOLS,
		},
	)


def welcome (request, repo_query):
	print repo_query
	return render_to_response ('relais.amergin/welcome.html',
		{
			'repos': repo_query,
			'inter_tools': INTER_TOOLS,
			'standalone_tools': STANDALONE_TOOLS,
		},
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


def vote (request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	print poll_id
	print p
	print request.POST['choice']
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the poll voting form.
		return render_to_response('polls/poll_detail.html', {
			  'object': p,
			  'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect (reverse('poll_results', args=(p.id,)))


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################


