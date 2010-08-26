#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SHORT DESCRIPTION

"""


### IMPORTS ###

from math import ceil

from django import template


## CONSTANTS & DEFINES ###

register = template.Library()


### IMPLEMENTATION ###

@register.filter
def formatseq (seq_str):
	"""
	Do a nice wrapped table for a sequence. As you do.
	"""
	line_width = 60
	block_width = 10
	line_cnt = ceil (float (len (seq_str)) / line_width)
	left_posns, right_posns = row_numbers (line_width, line_cnt)
	return """
<table class="sequence_layout" cellpadding="0" cellspacing="0">
  <tbody>
    <tr>
      <td class="line_numbers left">
        <pre>%s</pre>
      </td>
      <td class="sequence">
        <pre class="dna">%s</pre>
      </td>
      <td class="line_numbers right">
        <pre>%s</pre>
      </td>
    </tr>
  </tbody>
</table>
	""" % (left_posns, layout_seq (seq_str), right_posns)



# Layout a biosequence appropriate for display within HTML.
#
# [seq_str] the biosequence to be formatted, as a string
#
# [line_width] how long a line to 'wrap' the sequence in
# [block_width] the size of sections to break up a line into
#
# [returns] a 'naked' literal string to appear within a PRE or textarea
#
# A general layout technique for all biosequences. Numbering of positions
# must be handled elsewhere.
#
def layout_seq (seq_str, line_width=60, block_width=10, uppercase=True):
	## Main:
	if uppercase:
		seq_str = seq_str.upper()
	# break into lines & blocks
	lines = [seq_str[x:x+line_width] for x in range (0, len (seq_str), line_width)]
	blocked_lines = []
	for curr_line in lines:
		blocked_lines.append (' '.join ([curr_line[x:x+block_width] for x in
			range (0, len (curr_line), block_width)]))
	return '\n'.join (blocked_lines)


# Generate the position numbers for showing on the row ends of formatted bioseqs.
#
# [line_width] how wide is the sequence formatted
# [line_cnt] how many rows to supply numbers for
#
# [char_width] how many positions a single character is (3 for amino acids)
# [start_posn] what the first displayed position is
#
# [returns] two arrays, for the left and right sides respectively
#
def row_numbers (line_width, line_cnt, char_width=1, start_posn=1):
	## Main:
	posn_width = len (str (line_cnt * line_width * char_width))
	left_posns = '\n'.join (["%*s" % (posn_width, (e*line_width*char_width) +
		start_posn) for e in range (line_cnt)])
	right_posns = '\n'.join (["%*s" % (posn_width, ((e+1)*line_width*char_width) +
		(start_posn - char_width)) for e in range (line_cnt)])
	
	# Return:
	return left_posns, right_posns




### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ####################################################################

