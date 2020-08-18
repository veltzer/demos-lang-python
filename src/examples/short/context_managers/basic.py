"""
This is an example of creating your own resource to be used with the 'with'
python syntax. This is called a 'Context Manager'.

You can see the basic flow of code:
- first the constructor of your context manager is called.
- then your __enter__ code is called.
- then the users code block is executed.
- then your __exit__ code is called.
"""


class MyResource:

    def __init__(self):
        print("constructor")

    def __enter__(self):
        print("enter")

    def __exit__(self, _type, value, traceback):
        print("exit")


print("lets see a basic use of the context manager...")
with MyResource() as r:
    print("block of code")
