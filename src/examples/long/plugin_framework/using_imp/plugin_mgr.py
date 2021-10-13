# noinspection PyDeprecation
# pylint: disable=deprecated-module
import imp
import os
import os.path


# noinspection PyDeprecation
def load_module(module_ns, name, folder):
    info = imp.find_module(name, [folder])
    return imp.load_module(module_ns, *info)


def importPlugins(folder=None, ns=None):
    if ns is None:
        ns = folder
    files = os.listdir(folder)
    my_list = []
    for file in files:
        if file.endswith('.py'):
            name = file[:-3]
            module_ns = os.path.join(ns, name)
            m = load_module(module_ns, name, folder)
            my_list.append((name, module_ns, m))
    return my_list


def importPlugin(ns, path, name):
    '''
    This one imports a single plugin by name from a path giving path precedence
    '''
    for path_elem in path:
        test_file = os.path.join(path_elem, name + '.py')
        if os.path.isfile(test_file):
            load_module(ns, name, path_elem)
            return
    raise ValueError('plugin ' + name + ' not found')
