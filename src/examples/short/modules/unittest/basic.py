"""
This example demonstrates the use of the "unittest" module.
"""

import unittest


class MyUnitTest(unittest.TestCase):
    def test_this(self) -> None:
        current_sum = 0
        for x in range(100):
            current_sum += x
        assert current_sum == 4950


unittest.main()
