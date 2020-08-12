"""
This example shows that the python 'split' method on strings words
will full regular expressions.
"""

import re

s = 'there , is, a house in new, orleans 100,000,000  ,0000  456, 3.1415  this.is a sentence. and'

r = re.compile(r'(?<!\d),(?!\d)')

re_comma = r'(,)(?!\d)|(?<!\d)(,)'
re_dots = r'(\.)(?!\d)|(?<!\d)(\.)'
re_space = r'\s'

re_full = '|'.join([re_comma, re_dots, re_space])

l = re.split(re_full, s)
l = [x for x in l if x]
print(l)
