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
def my_mystery_function() -> None:
    # global g
    print(g)  # noqa: F823  teaching: shows a local name used before its assignment  # pyrefly: ignore[unbound-name]  teaching: g is local because it is assigned later in the function
    if True:
        g += 17
    print(g)


g = 4
# noinspection PyBroadException
try:
    my_mystery_function()
except UnboundLocalError:
    print("yes, got an exception")
print(g)
