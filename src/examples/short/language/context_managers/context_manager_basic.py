"""
This is an example of creating your own resource to be used with the "with"
python syntax. This is called a "Context Manager".

You can see the basic flow of code:
- first the constructor of your context manager is called.
- then your __enter__ code is called.
- then the users code block is executed.
- then your __exit__ code is called.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import TracebackType



class MyResource:

    def __init__(self) -> None:
        print("constructor")

    def __enter__(self) -> None:
        print("enter")

    def __exit__(self, exception_type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None:
        if value is not None:
            print("there was an exception")
            print(f"exception_type is {exception_type}")
            print(f"{value}")
            print(f"{type(value)}")
            print(f"{traceback}")
        else:
            print("there was no exception")


print("lets see a basic use of the context manager...")
with MyResource():
    print("block of code")
    raise ValueError(7)
