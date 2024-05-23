"""
This example shows how to use the "imp" module to do double importing of content
into the same namespace. You select the namespace, in this case "config".
"""

import importlib


one = importlib.import_module("folder1.module")
two = importlib.import_module("folder2.module")
