import functools
import os
import sys


def with_output_to(fname):
    """Make decorator to run with stdout redirected to fname.

    The file is opened for appending each time f will be called and
    closed when it returns.
    """

    def decorator(f):
        @functools.wraps(f)
        def decorated_f(*args, **kw):
            old_stdout = sys.stdout
            new_stdout = sys.stdout = open(fname, 'a')
            try:
                return f(*args, **kw)
            finally:
                sys.stdout = old_stdout
                new_stdout.close()

        return decorated_f

    return decorator


@with_output_to('/tmp/out2.txt')
def hello(name):
    print('Hello, {0}!'.format(name))


# Running this will destroy '/tmp/out2.txt'!

# make sure file is empty
open('/tmp/out2.txt', 'w').close()
# test
print('This should output nothing:')
hello('Fred')
hello('Barney')
print('The file now contains this:')
print(open('/tmp/out2.txt').read())
# clean up
os.remove('/tmp/out2.txt')
