"""
This example shows that you cannot change the value of a local variable indirectly
using the locals() or the vars() dictionaries.
You CAN,however,change the global variables...

Things to notice:
- inside the function vars and locals look the same.
- inside the function globals show the REAL globals (without override of the locals).
- inside the function you are still in the __main__ scope (__name__=='__main__').
"""


# noinspection PyShadowingNames
def func(x):
    y = 7
    print('x is ', x)
    print('y is ', y)
    print('z is ', z)
    print(vars())
    print(locals())
    print(globals())
    print(__name__)
    locals()['x'] = 9
    vars()['y'] += 1
    globals()['z'] += 1
    print('x is ', x)
    print('y is ', y)
    print('z is ', z)


x = 10
y = 20
z = 30
func(40)
print('x is', x)
print('y is', y)
print('z is', z)
