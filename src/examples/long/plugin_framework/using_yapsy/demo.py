"""
This is an example of using yapsy to create a lightweight plugin based system.

References:
http://yapsy.sourceforge.net
"""

import sys

import yapsy.PluginManager

simplePluginManager = yapsy.PluginManager.PluginManager()
# Tell it the default place(s) where to find plugins
simplePluginManager.setPluginPlaces(["plugins"])

print(
    "load all the plugins (this also calls the construction of IPlugin objects)")
simplePluginManager.collectPlugins()

print("now printing plugins info")
for pluginInfo in simplePluginManager.getAllPlugins():
    print(f"name is [{pluginInfo.name}]")
    print(f"description is [{pluginInfo.description}]")
    print(f"path is [{pluginInfo.path}]")
    print(f"plugin_object is [{pluginInfo.plugin_object}]")
    # here is how to get to the module the plugin is in
    module_obj = sys.modules[pluginInfo.plugin_object.__module__]
    print(f"var is [{module_obj.var}]")
    # debug starts here
    # print(dir(sys.modules[pluginInfo.plugin_object.__module__]))
    # print(dir(pluginInfo))
    # print(pluginInfo.__class__)
    # print(pluginInfo.__module__)

print("activate all the plugins")
for pluginInfo in simplePluginManager.getAllPlugins():
    simplePluginManager.activatePluginByName(pluginInfo.name)

print("do something with all plugins")
for pluginInfo in simplePluginManager.getAllPlugins():
    pluginInfo.plugin_object.do_something()

print("deactivate all the plugins")
for pluginInfo in simplePluginManager.getAllPlugins():
    simplePluginManager.deactivatePluginByName(pluginInfo.name)
