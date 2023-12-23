Write a context manager that redirects sys.stdout to a file for the duration of the block, and restores it on exit.

Note: compare this approach with the decorator approach. See how much simpler it is?
Conclusion: don't use decorators when a context manager would do.

this was redirection using a function decorator:

@redirect
def my_func():
    print("hello")

now we want the same thing but using a context manager and not a function decorator:

with RedirectManager("out.txt"):
    print("hello")
print("goodbye")

and magically the "hello" print would go to the "out.txt" file.
Once the block is over, the printing returns to it's original destination.
So in our case, "goodbye" would be printed to the screen.
