"""
A demo of how warnings work in python.

When should you issue a warning?
If you are a piece of code and you notice something abnormal, that probably
indicates a bug in the current running process or in the way your code is
being used by the user, then issue a warning.

You should only issue a warning if you can continue running despite the warning.
If you cannot continue to run, raise an exception.
"""

import warnings


def fxn():
    print('in the function')
    # warnings.warn('deprecated', DeprecationWarning)
    # warnings.warn('this is a warning', Warning)
    warnings.warn('this is a problem')


# with warnings.catch_warnings():
# warnings.simplefilter('ignore')
# warnings.filterwarnings('error')
warnings.filterwarnings('ignore')
fxn()
warnings.filterwarnings('error')
# warnings.resetwarnings()
fxn()
# warnings.warn('this is a problem')
fxn()
