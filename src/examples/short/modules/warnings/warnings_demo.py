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


def fxn() -> None:
    print("in the function")
    # warnings.warn("deprecated", DeprecationWarning)  # noqa: ERA001  teaching: kept in the comment for the reader
    # warnings.warn("this is a warning", Warning)  # noqa: ERA001  teaching: kept in the comment for the reader
    warnings.warn("this is a problem", stacklevel=2)


# with warnings.catch_warnings():
# warnings.simplefilter("ignore")  # noqa: ERA001  teaching: kept in the comment for the reader
# warnings.filterwarnings("error")  # noqa: ERA001  teaching: kept in the comment for the reader
warnings.filterwarnings("ignore")
fxn()
warnings.filterwarnings("error")
# warnings.resetwarnings()  # noqa: ERA001  teaching: kept in the comment for the reader
fxn()
# warnings.warn("this is a problem")  # noqa: ERA001  teaching: kept in the comment for the reader
fxn()
