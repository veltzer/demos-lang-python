"""
This is an example of using yapsy to create a lightweight plugin based system.

References:
http://yapsy.sourceforge.net
"""

import sys

import yapsy.PluginManager

simple_plugin_manager = yapsy.PluginManager.PluginManager()
# Tell it the default place(s) where to find plugins
simple_plugin_manager.setPluginPlaces(["plugins"])

print(
    "load all the plugins (this also calls the construction of IPlugin objects)")
simple_plugin_manager.collectPlugins()

print("now printing plugins info")
for plugin_info in simple_plugin_manager.getAllPlugins():
    print(f"name is [{plugin_info.name}]")
    print(f"description is [{plugin_info.description}]")
    print(f"path is [{plugin_info.path}]")
    print(f"plugin_object is [{plugin_info.plugin_object}]")
    # here is how to get to the module the plugin is in
    module_obj = sys.modules[plugin_info.plugin_object.__module__]
    print(f"var is [{module_obj.var}]")
    # debug starts here
    # print(dir(sys.modules[plugin_info.plugin_object.__module__]))
    # print(dir(plugin_info))
    # print(plugin_info.__class__)
    # print(plugin_info.__module__)

print("activate all the plugins")
for plugin_info in simple_plugin_manager.getAllPlugins():
    simple_plugin_manager.activatePluginByName(plugin_info.name)

print("do something with all plugins")
for plugin_info in simple_plugin_manager.getAllPlugins():
    plugin_info.plugin_object.do_something()

print("deactivate all the plugins")
for plugin_info in simple_plugin_manager.getAllPlugins():
    simple_plugin_manager.deactivatePluginByName(plugin_info.name)
