"""
This is a basic closure example.
"""


def make_counter(object):
    def tick():
        object["data"] = object["data"] + 1
        return object["data"]
    return tick 


counter = make_counter({"data": 5})

for _ in range(10):
    print(counter())

# now the object object is garbage collected
counter = None
