"""
This is an example of how to turn a json string to an object and
an object to a json string.
"""

import json

json_str = """{
    "one": "one value",
    "two": "two value"
}
"""

obj = json.loads(json_str)
obj["three"] = "three value"
del obj["two"]
s = json.dumps(obj)
print(s)
