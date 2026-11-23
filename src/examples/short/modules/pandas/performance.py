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
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


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


random_strings: list[str] = []


def create_random_strings():
    random_strings[:] = [str(i) for i in range(1000000, 1000000 + large_table_size)]


tables: dict[str, DataFrame] = {}


def create_string_table():
    columns = [
        "A",
        "B",
        "C",
    ]
    tables["df"] = DataFrame("", index=random_strings, columns=columns)


def create_set_from_strings():
    _ = set(random_strings)


def create_dict_from_strings():
    _ = {x: x for x in random_strings}


input("press any key...")
print(f"creating 15mil empty table [{timeit.timeit(create_large_table, number=1)}]")
input("press any key...")
print(f"creating 15mil different strings [{timeit.timeit(create_random_strings, number=1)}]")
input("press any key...")
print(f"creating 15mil string table indexed by the random strings [{timeit.timeit(create_string_table, number=1)}]")
input("press any key...")
print(f"creating 15mil set [{timeit.timeit(create_set_from_strings, number=1)}]")
input("press any key...")
print(f"creating 15mil dict [{timeit.timeit(create_dict_from_strings, number=1)}]")
input("press any key...")

# print("creating a random array ")
# print("querying about 15mil entries by key")


def more_stuff():
    size = 15000000
    random_words = list(map(lambda _: random_word(10), range(size)))  # noqa: C417
    df = tables["df"]
    print("after creation")
    print(type(random_words))
    print(len(random_words))
    print_data(df)  # pyrefly: ignore[bad-argument-type]
    df.iloc[0, 0] = "mark"
    df.iloc[0, 1] = "veltzer"

    print(df.to_numpy())
