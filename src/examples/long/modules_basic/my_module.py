import sys

print('hello from [{0}]'.format(__file__))

my_global = 42


def print_module_info():
    # noinspection PyUnusedLocal
    my_local = 42
    print('module variables are [{0}]'.format(vars()))
    sane_globals = {
        k: v for k, v in globals().items() if not k.startswith('__')}
    print('module globals are [{0}]'.format(sane_globals))
    print('module name is [{0}]'.format(__name__))
    print(
        'module object via sys.modules is [{0}]'.format(sys.modules[__name__]))
    sane_dict = {k: v for k, v in sys.modules[
        __name__].__dict__.items() if not k.startswith('__')}
    print('module __dict__ is [{0}]'.format(sane_dict))
