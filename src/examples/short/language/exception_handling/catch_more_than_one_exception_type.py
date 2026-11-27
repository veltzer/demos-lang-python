"""
This example shows how to catch more than one exception type in python.

The syntax is:
    except <tuple of exception types> as e:

References:
- https://rollbar.com/blog/python-catching-multiple-exceptions/
"""


def raise_it(a_type: type[RuntimeError | ValueError]):
    raise a_type("hello")


for x in ValueError, RuntimeError:
    try:
        raise_it(x)
    except (ValueError, RuntimeError) as e:
        print(type(e))
