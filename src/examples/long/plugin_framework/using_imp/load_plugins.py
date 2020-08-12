import plugin_mgr

# the easiest way to use
plugins = plugin_mgr.importPlugins(folder='plugins')

for (name, ns, plugin) in plugins:
    print('var in the module is [{0}]'.format(plugin.var))
    print('members of [{0}]'.format(name))
    for p, v in plugin.__dict__.items():
        if not p.startswith('__'):
            print('\t{0} -> {1}'.format(p, v))

# plugin_mgr.importPlugins(folder='plugins', ns='plugins')

# plugin_mgr.importPlugin('commulative_plugins', [ 'plugins1' , 'plugins2' ], 'plugin1')
# plugin_mgr.importPlugin('commulative_plugins', [ 'plugins1' , 'plugins2'
# ], 'plugin2')
