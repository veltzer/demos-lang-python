"""
A basic demo of pandas

This demos:
- creating frames
- adding data to frames
- getting data from frames
"""
import random
import string
import timeit

import numpy
from pandas import DataFrame


def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def print_data(data_frame: DataFrame):
    print(len(data_frame))
    print(type(data_frame))


large_table_size = 15000000


def create_large_table():
    columns = [
        "A",
        "B",
        "C",
    ]
    data_frames = DataFrame("", index=numpy.arange(large_table_size), columns=columns)
    del data_frames


random_strings = []


def create_random_strings():
    global random_strings
    random_strings = list(map(lambda i: str(i), range(1000000, 1000000 + large_table_size)))


df = None


def create_string_table():
    global df
    columns = [
        "A",
        "B",
        "C",
    ]
    df = DataFrame("", index=random_strings, columns=columns)


def create_set_from_strings():
    _ = {x for x in random_strings}


def create_dict_from_strings():
    _ = {x: x for x in random_strings}


input("press any key...")
print("creating 15mil empty table [{}]".format(timeit.timeit(create_large_table, number=1)))
input("press any key...")
print("creating 15mil different strings [{}]".format(timeit.timeit(create_random_strings, number=1)))
input("press any key...")
print("creating 15mil string table indexed by the random strings [{}]".format(
    timeit.timeit(create_string_table, number=1)))
input("press any key...")
print("creating 15mil set [{}]".format(timeit.timeit(create_set_from_strings, number=1)))
input("press any key...")
print("creating 15mil dict [{}]".format(timeit.timeit(create_dict_from_strings, number=1)))
input("press any key...")

# print("creating a random array ")
# print("querying about 15mil entries by key")

"""
size = 15000000
random_words = list(map(lambda _: random_word(10), range(size)))
print("after creation")
print(type(random_words))
print(len(random_words))
print_data(df)
for _ in range(size):
    df.set_value()
df.set_value(0, "A", "mark")
df.set_value(0, "B", "veltzer")

print(df.get_values())
"""
