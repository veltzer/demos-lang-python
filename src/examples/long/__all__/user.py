""" user.py """

# pylint: disable=relative-beyond-top-level,no-name-in-module
# type: ignore
from . import module

module.a()
try:
    module.b()
except NameError:
    print("yes got exception")
