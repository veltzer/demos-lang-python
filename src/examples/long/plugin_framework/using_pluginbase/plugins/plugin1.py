# type: ignore
# pylint: disable=relative-beyond-top-level
from .. import demo

print(f"[{__file__}] loading")

var = "plugin1_value"

extra_var_only_for_plugin1 = "extra_value_only_for_plugin1"


def do_something():
    print(f"[{__file__}] running")


class Plugin1Class(demo.BaseClass):
    pass
