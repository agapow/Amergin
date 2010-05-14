#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from django import forms

from basetool import BaseTool
from registry import register_tool

__all__ = [
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class LoadSeqsTool (BaseTool):
	identifier = "loadbseqs"
	title = "Load biosequences"
	description = """Perform a bulk upload of biosequences from a single file
		to the repository. A collection can be formed from the contents."""

	template = "tool.html"
	
	class ToolForm(forms.Form):
		seqfile = forms.FileField(
			label="Sequence file",
			help_text="A file containing an alignment or multiple sequences.",
		)
		use_ann_reader = forms.BooleanField(
			label="Use extended reader",
			help_text="""Interprete directions embedded in
				the comments or description section of a sequence
				as annotations in the resultant sequence.""",
			initial=False,
			required=False,
		)
		format = forms.ChoiceField(
			label="Sequence format",
			required=True,
			choices=[
				# val, label
				["auto-detect", "ext"],
				["fasta", "nexus"],
				["gb", "genbank"],				
			]
		)
		bseq_src = forms.CharField(
			label="Source",
			help_text="""Label any uploaded sequence with the supplied
				source. If the sequence already has a source, it will be
				overwritten.""",
			required=False,
			max_length=100,
		)
		bseq_desc = forms.CharField(
			label="Description",
			help_text="""This will label any uploaded sequence with the supplied
				description. If the sequence already has a source, it will be
				overwritten.""",
			required=False,
			max_length=100,
		)
		extra_ann = forms.CharField(
			label="Add annotation",
			help_text="""This will tag any uploaded sequence with the supplied
				annotation. If the sequence already has a value for that annotation,
				it will be overwritten.""",
			required=False,
			max_length=100,
		)
		overwrite_bseqs = forms.BooleanField(
			label="Overwrite biosequences",
			help_text="Replace any prexisting sequences with the same identifier.",
			initial=False,
			required=False,
		)

		make_collection = forms.BooleanField(
			label="Make collection",
			help_text="""Form a collection from the contents of this upload. The
				collection will """,
			initial=False,
			required=False,
		)
		collection_title = forms.CharField(
			label="Collection title",
			required=False,
			max_length=100,
		)
		collection_desc = forms.CharField(
			label="Collection description",
			required=False,
			max_length=100,
		)
		collection_src = forms.CharField(
			label="Collection source",
			required=False,
			max_length=100,
		)

		fieldsets = [
			(None,               {'fields': ['question']}),
			('Date information', {'fields': ['collection_desc']}),
		]
	
register_tool (LoadSeqsTool)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
