""" plugin1.py """

import yapsy.IPlugin

print(f"[{__file__}] loading")


class PluginOne(yapsy.IPlugin.IPlugin):
    def __init__(self) -> None:
        super().__init__()
        print(f"This is __init__ of {__name__}")

    def activate(self) -> None:
        print(f"{__name__} is activated")

    def deactivate(self) -> None:
        print(f"{__name__} is deactivated")

    def do_something(self) -> None:
        print(f"do_something for {__name__} {self}")


var = f"my variable value is [{__name__}]"
