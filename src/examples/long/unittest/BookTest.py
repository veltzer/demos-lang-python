""" BookTest.py """



import unittest

import Book  # type: ignore[import-not-found]


class BookTest(unittest.TestCase):
    # tests

    def setUp(self):
        print("in setUp")

    def tearDown(self):
        print("in tearDown")

    def test_basic(self):
        print("in test_basic")
        p = Book.Book(50)
        self.assertTrue(p.get_price() == 50)

    def test_more(self):
        print("in test_more")
        p = Book.Book(50)
        # pylint: disable=protected-access
        p._Book__price = 60  # pyrefly: ignore[missing-attribute]
        self.assertTrue(p.get_price() == 60)

    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        print("in test_skipped")

    def run_test(self):
        print("in run_test")
        p = Book.Book(50)
        # pylint: disable=protected-access
        p._Book__price = 60  # pyrefly: ignore[missing-attribute]
        self.assertTrue(p.get_price() == 60)


unittest.main()
