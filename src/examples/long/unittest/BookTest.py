""" BookTest.py """

# type: ignore

import unittest

import Book  # type: ignore[import-not-found]


class BookTest(unittest.TestCase):
    # tests

    def setUp(self):
        print("in setUp")

    def tearDown(self):
        print("in tearDown")

    def testBasic(self):
        print("in testBasic")
        p = Book.Book(50)
        self.assertTrue(p.get_price() == 50)

    def testMore(self):
        print("in testMore")
        p = Book.Book(50)
        # pylint: disable=protected-access
        p._Book__price = 60
        self.assertTrue(p.get_price() == 60)

    @unittest.skip("demonstrating skipping")
    def testSkipped(self):
        print("in testSkipped")

    def runTest(self):
        print("in runTest")
        p = Book.Book(50)
        # pylint: disable=protected-access
        p._Book__price = 60
        self.assertTrue(p.get_price() == 60)


unittest.main()
