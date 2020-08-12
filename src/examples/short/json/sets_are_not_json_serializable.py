"""
This example shows that python sets are not JSON serializable
"""

import json

my_set = {
    'one',
    'two',
}

filename = '/dev/null'

with open(filename, 'w') as file_handle:
    try:
        json.dump(my_set, file_handle)
    except TypeError:
        print("yes, got type error")
