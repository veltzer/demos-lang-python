import sys


print(f"hello from [{__file__}]")
my_global = 42


def print_module_info():
    # noinspection PyUnusedLocal
    # pylint: disable=unused-variable
    my_local = 42  # noqa: F841
    print(f"module variables are [{vars()}]")
    sane_globals = {k: v for k, v in globals().items() if not k.startswith("__")}
    print(f"module globals are [{sane_globals}]")
    print(f"module name is [{__name__}]")
    print(f"module object via sys.modules is [{sys.modules[__name__]}]")
    sane_dict = {k: v for k, v in sys.modules[__name__].__dict__.items() if not k.startswith("__")}
    print(f"module __dict__ is [{sane_dict}]")
