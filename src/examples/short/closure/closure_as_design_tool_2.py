"""
This is an example of information hiding in functions
"""


def make_print_something(s):
    def inner():
        print(s)

    return inner


print_hello = make_print_something('hello')
print_goodbye = make_print_something('goodbye')

print_hello()
print_goodbye()
print_hello()
print_goodbye()
print_hello()
print_hello()
