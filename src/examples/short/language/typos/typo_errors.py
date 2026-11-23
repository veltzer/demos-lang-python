"""
This is an example of what typo errors could cause in python.
This means that testing is more important in python than in
other languages. Note that the variable "val_to_incremnt" is
local (in javascript this would be even worse since it would
be global).
"""


def return_inc(val_to_increment):
    val_to_incremnt = val_to_increment + 1  # noqa: F841  teaching: the typo creates a new unused variable
    return val_to_increment


print(return_inc(5))
