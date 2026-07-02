"""
This is a basic closure example.
"""


def make_counter(x):
    val = [ x ]
    def tick():
        val[0] = val[0] +1
        return val[0]
    return tick


counter = make_counter(5)

for _ in range(10):
    print(counter())

# now the object object is garbage collected
counter = None
