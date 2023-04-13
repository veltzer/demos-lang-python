"""
This is an example of a singleton pattern in python.
Notice that since we cannot make the constructor private
we resort to making sure,inside the constructor code,
that we are not called a second time.

This example is not that pretty in that it does not use a
'real' static method of the A class to return the singleton
instance. See the next example for an improvement on this.

This 'getInstance' method is also not protected against multi
thread access. Again,see next examples for a more realistic
solution.

The problem with this example is that you can call the
constructor for A * without * the 'getInstance' method
(simply by a=A()) and in this case it will not be registered
as the instance (in A.instance). This can be fixed by moving
the registration into the constructor function itself.
"""
from typing import Union, Any


class A:
    instance: Union[Any, None] = None

    def __init__(self):
        if A.instance is not None:
            raise ValueError('you called the constructor twice!!')
        # constructor code goes here
        print('in A constructor')
        self.my_attribute = 'value'


def getInstance() -> A:
    if A.instance is None:
        A.instance = A()
    return A.instance


myA1 = getInstance()
myA2 = getInstance()
if myA1 is myA2:
    print('yes,they are the same instance')
print(dir(myA1))
