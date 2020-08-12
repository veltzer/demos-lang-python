"""
Question: what does this function output ?

Answer: exception.

If you remove the remark over 'global g' then
the 'g' variable is the same all over the program.

If you leave the remark over 'global g' then 'g'
inside 'my_mistery_function' is referenced before
it is assigned and you get an exception indicating
that.
"""


def my_mistery_function():
    # global g
    print(g)
    if False:
        g += 17
    print(g)


g = 4
try:
    my_mistery_function()
except:
    print('yes, got an exception')
print(g)
