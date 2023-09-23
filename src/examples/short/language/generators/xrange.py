"""
This is an example of doing our own range
"""


def my_range(fr, to, jump):
    while fr < to:
        yield fr
        fr += jump


for i in my_range(1, 13, 3):
    print(i)
