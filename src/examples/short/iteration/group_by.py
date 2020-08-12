"""
This is a demo of itertools.groupby
"""

import itertools


def indentation(line):
    return len(line) - len(line.lstrip())


data = '''this is no indent 1
this is no indent 2
    this is 1 indent 1
    this is 1 indent 2
this is no indent 3
this is no indent 4
    this is 1 indent 3
    this is 1 indent 4'''

for (indent, paragraph) in itertools.groupby(data.split('\n'), key=indentation):
    print('%d-spaced paragraph' % indent)
    for line in paragraph:
        print(line.strip())
