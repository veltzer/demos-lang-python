"""
This example shows how to use the 'imp' module to do double importing of content
into the same namespace. You select the namespace, in this case 'config'.
"""

# noinspection PyDeprecation
import imp

# noinspection PyDeprecation
config = imp.load_source('config', 'folder1/module.py')
print(config)
# noinspection PyDeprecation
config = imp.load_source('config', 'folder2/module.py')
print(config)

for var in config.__dict__:
    if not var.startswith('__'):
        print(var, config.__dict__[var])
