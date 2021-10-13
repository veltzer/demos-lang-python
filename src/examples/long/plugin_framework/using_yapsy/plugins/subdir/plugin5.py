import yapsy.IPlugin

print(f"[{__file__}] loading")


class PluginThree(yapsy.IPlugin.IPlugin):
    def __init__(self):
        super().__init__()
        print(f"This is __init__ of {__name__}")

    def activate(self):
        print(f"{__name__} is activated")

    # def deactivate(self):
    #     print(f"{__name__} is deactivated")

    # noinspection PyMethodMayBeStatic
    def do_something(self):
        print(f"do_something for {__name__}")


var = f"my variable value is [{__name__}]"
