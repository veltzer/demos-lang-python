""" plugin1.py """


import importlib

# the parent package of the plugins package (the same as "from .. import demo")
demo = importlib.import_module("..demo", package=__package__)

print(f"[{__file__}] loading")

var = "plugin1_value"

extra_var_only_for_plugin1 = "extra_value_only_for_plugin1"


def do_something():
    print(f"[{__file__}] running")


class Plugin1Class(demo.BaseClass):
    pass
