import base  # type: ignore

print(f"[{__file__}] loading")

var = "plugin1_value"

extra_var_only_for_plugin1 = "extra_value_only_for_plugin1"


def do_something():
    print(f"[{__file__}] running")


class Plugin1(base.BaseClass):
    def __init__(self):
        print("in init of Plugin1")
