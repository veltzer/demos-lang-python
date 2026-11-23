"""
This is an example of using pkgutil to create a lightweight plugin based system.
"""

import importlib.util
import pkgutil

do_debug = False
do_print_members = False

for module_loader, name, ispkg in pkgutil.iter_modules(path=["plugins"]):
    if do_debug:
        print(module_loader, name, ispkg)
    if not ispkg:
        spec = module_loader.find_spec(name, None)
        assert spec is not None
        assert spec.loader is not None
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
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
