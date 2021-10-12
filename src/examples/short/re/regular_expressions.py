"""
This is an example that demonstrates using regular expressions in python

NOTES:
- .match matches the *entire* string.
- .findall can return all matches as strings.
"""

import re

c = re.compile(r'^\tfoobar (\d+)\n$')

# lets get the match object
m = c.match('\tfoobar 17\n')
if m:
    print(f"m.group() is [{m.group()}]")
    print(f"m.group(1) is [{m.group(1)}]")
else:
    print("no match")

c = re.compile(r"foobar \d+")
my_list = c.findall('adfad foobar 20 sadfasd foobar 5 asdfasdfad foobar 3235')
print(my_list)
