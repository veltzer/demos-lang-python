#!/usr/bin/env python

"""
This example shows how to use operator.itemgetter to avoid writing
small lambda functions to achieve the same goal.

References:
http://stackoverflow.com/questions/22412258/get-the-first-element-of-each-tuple-in-a-list-in-python
"""

from operator import itemgetter

rows = [(1, 2), (3, 4), (5, 6)]
print(list(map(itemgetter(1), rows)))
