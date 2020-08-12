"""
This is quite an advanced example of doing meta programming in python.
This exercise shows how to:
    - add a method to a class
    - add a method to an instance.
"""

import pprint

from new import instancemethod


class Person:
    def __init__(self, name, fname):
        self.name = name
        self.fname = fname

    def printMe(self):
        print(self.name + ' ' + self.fname)


p = Person('Mark', 'Veltzer')
p.printMe()

b = Person('James', 'Bond')
b.printMe()


# lets define a function that looks like a method of person...


def secret_agent_output(self):
    print(self.fname + ',', self.name, self.fname)


# lets add this method only to the 'b' instance...
# this line does not work!
# b.printMe=secret_agent_output
# this works! turning a function into a method...
b.printMe = instancemethod(secret_agent_output, b, Person)
print('Only James is a secret agent...')
p.printMe()
b.printMe()

# now lets make everyone a secret agent...
# both of these will work (2nd version is better...)
# b.__class__.printMe=secret_agent_output
# Person.printMe=secret_agent_output
Person.printMe = instancemethod(secret_agent_output, None, Person)
print('Now we are both secret agents...')
b.printMe()
p.printMe()


# lets add a method new method to the class


def fire_your_berreta(self):
    print(self.name + ' is firing!')


Person.fire = fire_your_berreta

# lets kill some people
print('Now we both have firing capabilities...')
b.fire()
p.fire()

print('Here is some debug info:')
print('here is james...')
pprint.pprint(b.__dict__)
print('here is mark...')
pprint.pprint(p.__dict__)
print('here is the class definition...')
pprint.pprint(b.__class__)
pprint.pprint(b.__class__.__dict__)
