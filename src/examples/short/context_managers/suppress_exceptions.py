"""
This is an example of creating your own resource to be used with the 'with'
python syntax. This is called a 'Context Manager'.

NOTES:
- the retrun value of __exit__ is whether or not to suppress an exception
if such has happened.

TODO:
- show how to use the return value of __enter__
"""


class MyResource:
    enterCallsCounter = 0
    exitCallsCounter = 0

    def __init__(self, suppress=False):
        """ this is the constructor (the thing we call at the 'with') """
        self.suppress = suppress

    def __enter__(self):
        """ this method will be called at the begining of the 'with' block """
        print('doing __enter__')
        MyResource.enterCallsCounter += 1
        return self

    def __exit__(self, itype, value, traceback):
        """ this method will be called at the end of the 'with' block """
        print('doing __exit__', itype, value, traceback)
        MyResource.exitCallsCounter += 1
        return self.suppress


# first lets try to just see if enter and exit are called
with MyResource() as r:
    print(r)
    print('in block of code')
assert MyResource.enterCallsCounter == 1
assert MyResource.exitCallsCounter == 1
print(
    'yes,if we got this far it means that both enter and exit were called exactly one time during the last attempt')

# now lets try to throw an exception from the 'with' block and see that exit it called
try:
    with MyResource() as r:
        print(r)
        raise ValueError('foobar')
except ValueError:
    pass
assert MyResource.enterCallsCounter == 2
assert MyResource.exitCallsCounter == 2
print(
    'yes,if we got this far it means that both enter and exit were called exactly one time during the last attempt')

# now lets try to suppress the exception thrown
with MyResource(suppress=True) as r:
    print(r)
    # pylint: disable=broad-exception-raised
    raise Exception('foobar')
assert MyResource.enterCallsCounter == 3
assert MyResource.exitCallsCounter == 3
print(
    'yes,if we got this far it means that both enter and exit were called exactly one time during the last attempt')
