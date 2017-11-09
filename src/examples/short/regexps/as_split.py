#!/usr/bin/env python

"""
This example shows how to use python as a split replacement
"""

import re

print(re.findall(r'([A-Z][a-z]+)', 'ThisIsSometimeElse'))
