# pylint: disable=relative-beyond-top-level
from .. import demo

print(f"[{__file__}] loading")

var = 'plugin2_value'

extra_var_only_for_plugin2 = 'extra_value_only_for_plugin2'


def do_something():
    print(f"[{__file__}] running")


class Plugin2Class1(dict):
    pass


class Plugin2Class2(demo.BaseClass):
    pass
