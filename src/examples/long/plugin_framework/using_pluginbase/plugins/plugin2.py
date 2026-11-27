""" plugin2.py """


import importlib

# the parent package of the plugins package (the same as "from .. import demo")
demo = importlib.import_module("..demo", package=__package__)

print(f"[{__file__}] loading")

var = "plugin2_value"

extra_var_only_for_plugin2 = "extra_value_only_for_plugin2"


def do_something() -> None:
    print(f"[{__file__}] running")


class Plugin2Class1(dict[str, str]):
    pass


class Plugin2Class2(demo.BaseClass):
    pass
