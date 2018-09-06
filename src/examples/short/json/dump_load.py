#!/usr/bin/env python

"""
This example explores loading/saving dictionaries in python from/to files

Notes:
- python sets are not JSON serializable (see another example)
"""

import json

my_dict = {
    'one': 'one value',
    'two': 'two value',
}

filename = '/tmp/json_store.json'

with open(filename, 'w') as file_handle:
    json.dump(my_dict, file_handle, indent=4)

with open(filename) as file_handle:
    other_dict = json.load(file_handle)

assert my_dict == other_dict, "dictionaries are not the same"
