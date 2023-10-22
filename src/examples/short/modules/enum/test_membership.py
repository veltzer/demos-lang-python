"""
This is an example of how to test if something is a member if this enum
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
        print("yes")
    else:
        print("no")


# passing numbers is no good, we need to pass the real values
is_enum(7)
is_enum(Event.edge_pre_del)
