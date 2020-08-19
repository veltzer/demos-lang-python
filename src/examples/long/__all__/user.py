from . import module

module.a()
try:
    module.b()
except NameError:
    print("yes got exception")
