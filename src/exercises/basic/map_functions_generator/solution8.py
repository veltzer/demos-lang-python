"""
Solution but with a variable argument list
"""

import operator


def apply_funcs(lst, *args, **kwargs):
    return [f(*args, **kwargs) for f in lst]


print(apply_funcs([operator.add, operator.sub], 5, 4))
