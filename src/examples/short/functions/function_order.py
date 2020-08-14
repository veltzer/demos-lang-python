"""
This example explores correct function order in the source code.

This means that a function cannot be used until after it has been defined.
"""

# this is wrong since foo is not defined
# noinspection PyBroadException
try:
    foo()
except:
    print('yep, this failed')


def foo():
    print('this is foo')
    bar()


# this will call foo but will fail once foo tried to call bar
# noinspection PyBroadException
try:
    foo()
except:
    print('yep, this failed')


def bar():
    print('this is bar')


# this should work now that both 'foo' and 'bar' are defined
foo()

del bar

# now that 'bar' is no longer defined any call to 'foo' should fail
try:
    foo()
except:
    print('yep, this failed')
