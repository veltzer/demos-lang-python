""" demo.py """

import inspect

from pluginbase import PluginBase


class BaseClass:
    pass


def main():
    plugin_base = PluginBase(package="plugins")
    plugin_source = plugin_base.make_plugin_source(searchpath=["plugins"])
    for plugin in plugin_source.list_plugins():
        p = plugin_source.load_plugin(plugin)
        p.do_something()
        for k, v in p.__dict__.items():
            if not inspect.isclass(v):
                continue
            print(type(v))
            if issubclass(v.__class__, BaseClass.__class__):
                print(k)


if __name__ == "__main__":
    main()
