"""
An example of an 'id generator' using two ways:
1) simple global variable
2) hiding the data in a closure.
3) function attribute

* Notice that the closure must be a list or object and not a primitive
since a primitive will be a local variable in 'give_me_unique'.
"""

# first example
counter = 0


def give_me_a_unique_value():
    # pylint: disable=global-statement
    global counter
    counter += 1
    return counter


print(give_me_a_unique_value())
print(give_me_a_unique_value())
print(give_me_a_unique_value())


# second example


def give_me_unique_generator():
    my_list = [0]

    def give_me_unique():
        my_list[0] += 1
        return my_list[0]

    return give_me_unique


g = give_me_unique_generator()
print(g())
print(g())
print(g())


# third example


def give_me_a_unique_value2():
    give_me_a_unique_value2.counter += 1
    return give_me_a_unique_value2.counter


give_me_a_unique_value2.counter = 0
print(give_me_a_unique_value2())
print(give_me_a_unique_value2())
print(give_me_a_unique_value2())
