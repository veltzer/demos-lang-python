"""
This is a basic closure example.
"""


def make_counter(o):
    def tick():
        o["data"] = o["data"] + 1
        return o["data"]
    return tick


counter = make_counter({"data": 5})

for _ in range(10):
    print(counter())

# now the object object is garbage collected
counter = None
