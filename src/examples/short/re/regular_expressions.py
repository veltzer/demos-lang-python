"""
This is an example that demonstrates using regular expressions in python

NOTES:
- .match matches the *entire* string.
- .findall can return all matches as strings.
"""

import re

c = re.compile('^\tfoobar (\d+)\n$')

# lets get the match object
m = c.match('\tfoobar 17\n')
if m:
    print('m.group() is [{g}]'.format(g=m.group()))
    print('m.group(1) is [{g}]'.format(g=m.group(1)))
else:
    print('no match')

c = re.compile('foobar \d+')
l = c.findall('adfad foobar 20 sadfasd foobar 5 asdfasdfad foobar 3235')
print(l)
