"""
This example shows how to create a test suite object with dynamically
created tests.

References:
- https://kite.com/examples/python/4920
"""

import unittest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def test_generator(a: int) -> Callable[[], None]:
    def test() -> None:
        assert a % 2 == 0

    return test


suite = unittest.TestSuite()
test_cases = [2, 4]
for case in test_cases:
    suite.addTest(
        unittest.FunctionTestCase(
            test_generator(case)))

unittest.TextTestRunner().run(suite)
