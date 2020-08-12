"""
This example of how to wrap a dictionary to look like a namespace
"""


class D(dict):
    def __init__(self):
        super(D, self).__init__()

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, val):
        self[name] = val


a = D()
a['one'] = 'one_value'
a.two = 'two_value'

print(a['one'])
print(a.one)

print('listing all entries in the object')
for k, v in a.items():
    print(k, v)
