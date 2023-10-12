import plugin_mgr  # type: ignore

# the easiest way to use
plugins = plugin_mgr.importPlugins(folder="plugins")

for name, ns, plugin in plugins:
    print(f"var in the module is [{plugin.var}]")
    print(f"members of [{name}]")
    for p, v in plugin.__dict__.items():
        if not p.startswith("__"):
            print(f"\t{p} -> {v}")

# plugin_mgr.importPlugins(folder="plugins", ns="plugins")

# plugin_mgr.importPlugin("cumulative_plugins", [ "plugins1" , "plugins2" ], "plugin1")
# plugin_mgr.importPlugin("cumulative_plugins", [ "plugins1" , "plugins2"
# ], "plugin2")
