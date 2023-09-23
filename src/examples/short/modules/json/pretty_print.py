"""
This example shows how to pretty print json using the "json" module.

References:
- https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
"""

import json
import sys

my_dict = {
    "one": "one value",
    "two": "two value",
}

print(json.dumps(my_dict, indent=4, sort_keys=True))
# or
json.dump(my_dict, sys.stdout, indent=4, sort_keys=True)
