"""
Solution but with a variable argument list
"""

import operator
from typing import Any


def apply_funcs(lst: list[Any], *args: Any, **kwargs: Any):
    return [f(*args, **kwargs) for f in lst]


print(apply_funcs([operator.add, operator.sub], 5, 4))
