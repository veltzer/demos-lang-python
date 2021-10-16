"""
Demo to show the usage of the imp module in python
This clearly shows that you can reload any module into any name space using
the imp module.
"""

# noinspection PyDeprecation, PyPep8
# pylint: disable=deprecated-module
import imp
import math

# noinspection PyDeprecation
imp.load_source("__main__", "using_imp_one.py")
# pylint: disable=undefined-variable
print(f"add(2,2) is {add(2, 2)}")  # noqa: F821
# noinspection PyDeprecation
imp.load_source("__main__", "using_imp_two.py")
# pylint: disable=undefined-variable
print(f"add(2,2) is {add(2, 2)}")  # noqa: F821

print(f"math.sin(0.5) is {math.sin(0.5)}")
# noinspection PyDeprecation
imp.load_source("math", "using_imp_three.py")
print(f"math.sin(0.5) is {math.sin(0.5)}")
