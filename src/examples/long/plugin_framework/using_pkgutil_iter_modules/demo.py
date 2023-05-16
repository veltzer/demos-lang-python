"""
This is an example of using pkgutil to create a lightweight plugin based system.
"""

import pkgutil

do_debug = False
do_print_members = False

for module_loader, name, ispkg in pkgutil.iter_modules(path=["plugins"]):
    if do_debug:
        print(module_loader, name, ispkg)
    if not ispkg:
        ml = module_loader.find_loader(name)[0]  # type: ignore
        m = ml.load_module()  # type: ignore
        if do_debug:
            print(type(m))
            print(dir(m))
            print(f"var in that module is [{m.var}]")
        m.do_something()
        if do_print_members:
            print(f"members of [{name}]")
            for p, v in m.__dict__.items():
                if not p.startswith("__"):
                    print(f"\t{p} -> {v}")
