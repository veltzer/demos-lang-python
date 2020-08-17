"""
Example of an enum in python3
"""

import enum


class Event(enum.Enum):
    node_pre_add = 1
    node_post_add = 2
    node_pre_del = 3
    node_post_del = 4
    edge_pre_add = 5
    edge_post_add = 6
    edge_pre_del = 7
    edge_post_del = 8
    node_pre_build = 9
    node_post_build = 10


def is_enum(member):
    if isinstance(member, Event):
        print('yes')
    else:
        print('no')


# passing numbers is no good, we need to pass the real values
is_enum(7)
is_enum(Event.edge_pre_del)

print(Event.edge_pre_del)
print(dir(Event.edge_pre_del))
print(dir(Event))
print('name is [{name}] and type is [{type}]'.format(
    name=Event.edge_pre_del.name,
    type=type(Event.edge_pre_del.name),
))
print('value is [{value}] and type is [{type}]'.format(
    value=Event.edge_pre_del.value,
    type=type(Event.edge_pre_del.value),
))

print("listing all values of the enum...")
for x in Event:
    print(x)
    print(x.name)
    print(x.value)

# translate from string to number
print(Event["edge_pre_del"])
