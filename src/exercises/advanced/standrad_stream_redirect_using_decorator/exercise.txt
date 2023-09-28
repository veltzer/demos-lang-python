Write a decorator that redirects sys.stdout to the file "out.txt" for the duration of the function, and restores the original value when it returns:

@with_output_to_out_txt
def f():
 ...

For simplicity, you can assume the decorated function takes no parameters.

Bonus:
Make the decorator be able to receive the file name as a parameter:

@with_output_to("out.txt")
def f():
 ...

Hint: it's a function that returns a decorator!
So you'll probably have 3 functions nested inside each other...
