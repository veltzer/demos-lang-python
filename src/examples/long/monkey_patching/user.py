""" user.py """

import mod_a_1  # type: ignore
import mod_b_1  # type: ignore


# lets call the regular version of the function
print("before hacking")
mod_b_1.func_b_1()

# lets patch
print("after hacking")


def hacked1():
    print("hacked1")


mod_a_1.func_a_1 = hacked1
mod_b_1.func_b_1()

# pylint: disable=wrong-import-position
import mod_b_2  # type:ignore # noqa: E402
import mod_a_2  # type:ignore # noqa: E402

# lets call the regular version of the function
print("before hacking")
mod_b_2.func_b_2()

# lets patch
print("after hacking")


def hacked2():
    print("hacked2")


mod_a_2.func_a_2 = hacked2
mod_b_2.func_b_2()

print("mmm, didnt work. Trying to patch modb directly")
mod_b_2.func_a_2 = hacked2
mod_b_2.func_b_2()
