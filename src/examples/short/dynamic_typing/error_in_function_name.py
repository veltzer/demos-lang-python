"""
This is an example of how an error in a function name can cause problems.
The idea is that pythong does not check the name of the function "do_somethin"
until it reaches that line at runtime.
"""

# import time

def do_something():
    print("Hello")


print("hi")
# time.sleep(3600)
do_somethin()
