# pylint: disable=relative-beyond-top-level,no-name-in-module
# type: ignore
from . import my_module
print(f"hello from [{__file__}]")
my_module.print_module_info()
