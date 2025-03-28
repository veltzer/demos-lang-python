""" mod_b_2.py """

from mod_a_2 import func_a_2  # type: ignore


def func_b_2():
    print("func_b_2")
    func_a_2()
