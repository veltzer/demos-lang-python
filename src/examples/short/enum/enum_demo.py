"""
Example of an enum in python3
"""

import enum


class Event(enum.Enum):
    nodepreadd = 1
    nodepostadd = 2
    nodepredel = 3
    nodepostdel = 4
    edgepreadd = 5
    edgepostadd = 6
    edgepredel = 7
    edgepostdel = 8
    nodeprebuild = 9
    nodepostbuild = 10


def is_enum(x):
    if isinstance(x, Event):
        print('yes')
    else:
        print('no')


# passing numbers is no good, we need to pass the real values
is_enum(7)
is_enum(Event.edgepredel)

print(Event.edgepredel)
print(dir(Event.edgepredel))
print(dir(Event))
print('name is [{name}] and type is [{type}]'.format(
    name=Event.edgepredel.name,
    type=type(Event.edgepredel.name),
))
print('value is [{value}] and type is [{type}]'.format(
    value=Event.edgepredel.value,
    type=type(Event.edgepredel.value),
))

print("listing all values of the enum...")
for x in Event:
    print(x)
    print(x.name)
    print(x.value)

# tanslate from string to number
print(Event["edgepredel"])
