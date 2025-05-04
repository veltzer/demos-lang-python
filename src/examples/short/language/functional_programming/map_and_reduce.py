"""
A basic python functional "reduce" example
"""

from functools import reduce


raw_data = range(0, 100)

squares = map(lambda x: x * x, raw_data)

final_result = reduce(lambda a,b: a + b, squares)

print(final_result)
