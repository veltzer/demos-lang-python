"""
This is a basic closure example.
"""


def make_counter(x):
    val = [ x ]
    def tick():
        l = val[0]
        l = l + 1
        val[0] = l
        return l
    return tick 


counter = make_counter(5)

for _ in range(10):
    print(counter())

# now the object object is garbage collected
counter = None
