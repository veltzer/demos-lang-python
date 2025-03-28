""" mod_b_1.py """

import mod_a_1  # type: ignore


def func_b_1():
    print("func_b_1")
    mod_a_1.func_a_1()
