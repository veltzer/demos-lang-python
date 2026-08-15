"""
A basic python functional "reduce" example
"""

from functools import reduce

raw_data = range(100)

squares = map(lambda x: x * x, raw_data)  # noqa: C417

final_result = reduce(lambda a,b: a + b, squares)

print(final_result)
