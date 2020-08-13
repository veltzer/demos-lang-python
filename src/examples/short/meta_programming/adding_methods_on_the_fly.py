"""
This is quite an advanced example of doing meta programming in python.
This exercise shows how to:
    - add a method to a class
    - add a method to an instance.
"""

import pprint


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_me(self):
        print(self.name + ' ' + self.surname)


p = Person('Mark', 'Veltzer')
p.print_me()

b = Person('James', 'Bond')
b.print_me()


# lets define a function that looks like a method of person...


def secret_agent_output(self):
    print(self.surname + ',', self.name, self.surname)


# lets add this method only to the 'b' instance...
# this line does not work!
# b.printMe=secret_agent_output
# this works! turning a function into a method...
b.print_me = instancemethod(secret_agent_output, b, Person)
print('Only James is a secret agent...')
p.print_me()
b.print_me()

# now lets make everyone a secret agent...
# both of these will work (2nd version is better...)
# b.__class__.printMe=secret_agent_output
# Person.printMe=secret_agent_output
Person.print_me = instancemethod(secret_agent_output, None, Person)
print('Now we are both secret agents...')
b.print_me()
p.print_me()


# lets add a method new method to the class


def fire_your_gun(self):
    print(self.name + ' is firing!')


Person.fire = fire_your_gun

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
