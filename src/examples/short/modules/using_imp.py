"""
Demo to show the usage of the imp module in python
This clearly shows that you can reload any module into any name space using
the imp module.
"""

# noinspection PyDeprecation
import imp

# noinspection PyDeprecation
imp.load_source('__main__', 'using_imp_one.py')
print('add(2,2) is', add(2, 2))
# noinspection PyDeprecation
imp.load_source('__main__', 'using_imp_two.py')
print('add(2,2) is', add(2, 2))

# noinspection PyPep8
import math

print('math.sin(0.5) is', math.sin(0.5))
# noinspection PyDeprecation
imp.load_source('math', 'using_imp_three.py')
print('math.sin(0.5) is', math.sin(0.5))
