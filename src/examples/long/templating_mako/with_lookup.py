#!/usr/bin/env python

import datetime
import sys

import mako.lookup


def years(x):
    curr_year = datetime.datetime.now().year
    return ','.join(map(str, range(x, curr_year + 1)))


d = {
    'a': 'b',
    'c': 'd',
}

input_encoding = 'utf-8'
output_encoding = 'utf-8'
p_input = 'src/examples/long/templating_mako/simple.mako'
p_output = '/tmp/simple'

mylookup = mako.lookup.TemplateLookup(
    directories=['.'],
    input_encoding=input_encoding,
    output_encoding=output_encoding,
)
template = mako.template.Template(
    filename=p_input,
    #lookup=mylookup,
    #output_encoding=output_encoding,
    #input_encoding=input_encoding,
)
# the order here is importat. Do not open the file for writing until the rendering
# is complete since we want to make sure that the rendering process does not throw
# an exception. Only then do we open the file for writing.
# otherwise we will leave behind a partially written file and force the user
# to fix his makefile to remove the cruft we left behind...
output = template.render(foo='bar', years=years, d=d)
with open(p_output, 'w') as file_handle:
    file_handle.write(output)
