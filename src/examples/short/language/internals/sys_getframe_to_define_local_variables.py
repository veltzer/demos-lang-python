"""
This example shows how you can manipulate via sys._getframe any stack
frame including your own
"""




import sys

# define a new local variable "foo" and assign the value "42" to it...
# noinspection PyProtectedMember
sys._getframe().f_locals["foo"] = 42  # noqa: SLF001  teaching: demonstrating sys._getframe
print(foo)  # noqa: F821  teaching: foo is defined through the frame locals  # pyrefly: ignore[unknown-name]  teaching: foo is defined through the frame locals


def f() -> None:
    x = ["one"]
    print(f"val before is {x[0]}")
    g()
    print(f"val after is {x[0]}")


def g() -> None:
    # noinspection PyProtectedMember
    sys._getframe(1).f_locals["x"][0] = 42  # noqa: SLF001  teaching: demonstrating sys._getframe


f()
