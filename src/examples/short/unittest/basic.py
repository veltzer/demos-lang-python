"""
This example demonstrates the use of the "unittest" module.
"""

import unittest


class MyUnitTest(unittest.TestCase):
    def testThis(self):
        current_sum = 0
        for x in range(0, 100):
            current_sum += x
        self.assertEqual(current_sum, 4950)


unittest.main()
