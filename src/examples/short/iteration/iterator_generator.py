"""
This example shows that every generator in python can
be used as an iterator.

This is one of the ways in which you can write an iterator
in python.
"""


def my_reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in my_reverse("golf"):
    print(char)

# Notice that "my_reverse" is still recognized as a plain function and not
# "generator" or something.
# When you do use it for data the return value is a "generator".
# Compare this to pythons own "reversed" generator:
# - it is built in so its type is type
# - when using it as a generator its type is "reversed".

print(type(my_reverse))
print(type(my_reverse("golf")))
print(type(reversed))
print(type(reversed("golf")))
