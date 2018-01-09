#!/usr/bin/env python

import unittest

import Book


class BookTest(unittest.TestCase):
    # tests

    def setUp(self):
        print('in setUp')

    def tearDown(self):
        print('in tearDown')

    def testBasic(self):
        print('in testBasic')
        p = Book.Book(50)
        self.assertTrue(50 == p.get_price())

    def testMore(self):
        print('in testMore')
        p = Book.Book(50)
        p._Book__price = 60
        self.assertTrue(60 == p.get_price())

    @unittest.skip("demonstrating skipping")
    def testSkipped(self):
        print('in testSkipped')

    def runTest(self):
        print('in runTest')
        p = Book.Book(50)
        p._Book__price = 60
        self.assertTrue(60 == p.get_price())


unittest.main()
