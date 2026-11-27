"""
This is a *fast* singleton in that you pay only for the first call.
All subsequent calls don"t even have an "if" statement in them...

We also compare the difference in speed between the variation with
the if statement and without.

The result is that there is about 10% difference in performance
between the two methods.
"""

import time


class A:
    def __init__(self) -> None:
        pass


a_instance = None


def get_a_instance() -> A:  # noqa: F811  teaching: the function replaces itself through the global
    # noinspection PyGlobalUndefined
    global a_instance, get_a_instance  # noqa: PLW0603  teaching: the singleton is kept in a global
    if a_instance is None:
        a_instance = A()

    def get_a_instance_fast() -> A:
        return a_instance

    get_a_instance = get_a_instance_fast
    return a_instance


A1 = get_a_instance()
A2 = get_a_instance()
print(type(A1))
print(type(A2))
print(A1)
print(A2)
if A1 is A2:
    print("yes,they are the same instance")


class B:
    def __init__(self) -> None:
        pass


b_instance = None


def get_b_instance() -> B:
    global b_instance  # noqa: PLW0603  teaching: the singleton is kept in a global
    if b_instance is None:
        b_instance = B()
    return b_instance


B1 = get_b_instance()
B2 = get_b_instance()
print(type(B1))
print(type(B2))
print(B1)
print(B2)
if B1 is B2:
    print("yes,they are the same instance")

# sys.exit(0)  # noqa: ERA001  teaching: kept in the comment for the reader

# now lets measure times
num = 10000000
time_before = time.time()
for _ in range(num):
    a = get_a_instance()
time_after = time.time()
print(f"time for A: {time_after - time_before:.3f} seconds")
time_before = time.time()
# noinspection PyRedeclaration
for _ in range(num):
    b = get_b_instance()
time_after = time.time()
print(f"time for B: {time_after - time_before:.3f} seconds")
