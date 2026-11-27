"""
This is an example of how an error in a function name can cause problems.
The idea is that pythong does not check the name of the function "do_somethin"
until it reaches that line at runtime.
"""

# import time  # noqa: ERA001  teaching: kept in the comment for the reader


def do_something():
    print("Hello")


print("hi")
# time.sleep(3600)  # noqa: ERA001  teaching: kept in the comment for the reader
do_somethin()  # noqa: F821  teaching: the typo is only found at runtime  # pyrefly: ignore[unknown-name]  teaching: the typo is only found at runtime
