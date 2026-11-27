""" plugin2.py """

import yapsy.IPlugin

print(f"[{__file__}] loading")


class PluginTwo(yapsy.IPlugin.IPlugin):
    def __init__(self) -> None:
        super().__init__()
        print(f"This is __init__ of {__name__} {self}")

    # def activate(self):
    #     print(f"{__name__} is activated")  # noqa: ERA001  teaching: kept in the comment for the reader

    def deactivate(self) -> None:
        print(f"{__name__} is deactivated {self}")

    def do_something(self) -> None:
        print(f"do_something for {__name__} {self}")


var = f"my variable value is [{__name__}]"
