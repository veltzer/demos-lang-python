""" test_hello.py """

import tests.mod  # type: ignore


def test_hello():
    tests.mod.shared_method()
