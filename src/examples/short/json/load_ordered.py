#!/usr/bin/env python

"""
This example shows how you can load a json object in an ordered fashion (deterministic
across different python runs)

In order to see how this script works you need to run it several times in order
to see that sometimes the dictionary comes out right and sometimes not.

References:
- https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict-in-python
"""

import json
from collections import OrderedDict

raw_data = '{"foo":1, "bar": 2}'
data1 = json.loads(raw_data, object_pairs_hook=OrderedDict)
data2 = json.loads(raw_data)
print("ordered")
print(json.dumps(data1, indent=4))
print("unordered")
print(json.dumps(data2, indent=4))
