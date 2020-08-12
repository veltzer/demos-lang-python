"""
This is an example of using pkgutil to create a lightweight plugin based system.
"""

import pkgutil

do_debug = False
do_print_members = False

for (module_loader, name, ispkg) in pkgutil.iter_modules(path=['plugins']):
    if do_debug:
        print(module_loader, name, ispkg)
    if not ispkg:
        ml = module_loader.find_module(name)
        m = ml.load_module()
        if do_debug:
            print(type(r))
            print(dir(r))
            print('var in that module is [{0}]'.format(m.var))
        m.do_something()
        if do_print_members:
            print('members of [{0}]'.format(name))
            for p, v in m.__dict__.items():
                if not p.startswith('__'):
                    print('\t{0} -> {1}'.format(p, v))
