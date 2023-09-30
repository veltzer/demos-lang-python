"""
This example explores how jsonpickle serializes the most basic types
"""

import jsonpickle


o1 = {
    "France": "Paris",
    "Italy": "Rome",
}
print(o1)

# Serialize the instance to JSON using jsonpickle
json_str = jsonpickle.encode(o1)
print(json_str)

o2 = jsonpickle.decode(json_str)
print(o2)

print(o1 == o2)
