"""
This example shows how to use the "enumerate" iterator.

Notes:
- enumerate is supposed to be efficient both in python2.7
and in python3 although I havent checked that.
- the two code samples below do the same but the second
is more beautiful.
"""


# our own "enumerate"
def simple_enumerate(value_list):
    i = 0
    for val in value_list:
        yield i, val
        i += 1


def main():
    value_list = ["a", "b", "c"]
    # the non pythonic way to do this
    # pylint: disable=consider-using-enumerate
    for i in range(len(value_list)):
        print(i, value_list[i])
    # the pythonic way to do this
    for i, c in enumerate(value_list):
        print(i, c)
    # now let"s use our own enumerator
    for i, c in simple_enumerate(value_list):
        print(i, c)


main()
