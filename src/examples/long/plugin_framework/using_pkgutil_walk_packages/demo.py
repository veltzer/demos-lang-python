# type: ignore
"""
This is an example of using pkgutil to create a lightweight plugin based system.

Here is how you would use a fully well designed object like this:

import whatever

mgr=plugger.mgr.Mgr()
mgr.load_plugins(folder)
mgr.collect_and_instantiate(myBaseClass1)
mgr.collect_and_instantiate(myBaseClass2)
for instance in mgr.giveMe(myBaseClass1):
    ...
"""


import importlib
import pkgutil

# pylint: disable=relative-beyond-top-level, no-name-in-module
from . import base

do_debug = False
do_print_members = False

folder = 'plugins'
namespace = 'plugins.'

done = set()
for importer, modname, is_package in pkgutil.walk_packages(
        path=[folder],
        prefix=namespace,
):
    try:
        if modname in done:
            continue
        module_obj = importlib.import_module(modname)
        done.add(modname)
        print(done)
        print(f"imported {modname}")
        for name, t in module_obj.__dict__.items():
            # if type(t) is type and issubclass(t, base.BaseClass):
            if isinstance(t, base.BaseClass):
                instance = t()
                print(name)
                print(t)
                print(instance)
    except Exception as e:
        raise e
