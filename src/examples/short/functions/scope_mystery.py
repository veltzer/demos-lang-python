"""
Question: what does this function output ?

Answer: exception.

If you remove the remark over "global g" then
the "g" variable is the same all over the program.

If you leave the remark over "global g" then "g"
inside "my_mistery_function" is referenced before
it is assigned and you get an exception indicating
that.
"""


# noinspection PyUnboundLocalVariable
def my_mystery_function():
    # global g
    # pylint: disable=redefined-outer-name,used-before-assignment
    print(g)
    # pylint: disable=using-constant-test
    if True:
        g += 17  # noqa: F823
    print(g)


g = 4
# noinspection PyBroadException
try:
    my_mystery_function()
except UnboundLocalError:
    print("yes, got an exception")
print(g)
