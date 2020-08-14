"""
This example explores what happens when you just 'raise' without parameters.

The difference is that when you 'raise' with an exception the place where
you raise is added to the stack trace of the exception. If this is a new
exception that you create
"""

# you cannot just raise without a prior exception being active
try:
    raise
except RuntimeError as e:
    print('All is ok. you cannot raise without a prior active exception [{}]'.format(e))


def traceback_len(tb):
    count = 0
    while tb.tb_next:
        count += 1
        tb = tb.tb_next
    return count


# lets try to raise without an exception
try:
    try:
        raise ValueError('hello')
    except ValueError as e:
        raise
except ValueError as e:
    tb = e.__traceback__
    assert traceback_len(tb) == 0

# lets try to raise with an exception
try:
    try:
        raise ValueError('hello')
    except ValueError as e:
        raise e
except ValueError as e:
    tb = e.__traceback__
    assert traceback_len(tb) == 1
