""" BookTest.py """



import unittest

import Book  # pyrefly: ignore[missing-import]  teaching: sibling module found via the script directory when run by run_all.sh, not on the project search path


class BookTest(unittest.TestCase):
    # tests

    def setUp(self):
        print("in setUp")

    def tearDown(self):
        print("in tearDown")

    def test_basic(self):
        print("in test_basic")
        p = Book.Book(50)
        assert p.get_price() == 50

    def test_more(self):
        print("in test_more")
        p = Book.Book(50)
        p._Book__price = 60  # noqa: SLF001  teaching: the test sets the name-mangled private field directly
        assert p.get_price() == 60

    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        print("in test_skipped")

    def run_test(self):
        print("in run_test")
        p = Book.Book(50)
        p._Book__price = 60  # noqa: SLF001  teaching: the test sets the name-mangled private field directly
        assert p.get_price() == 60


unittest.main()
