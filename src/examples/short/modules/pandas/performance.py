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

import numpy as np
from pandas import DataFrame


def random_word(length: int) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def print_data(data_frame: DataFrame) -> None:
    print(len(data_frame))
    print(type(data_frame))


large_table_size = 15000000


def create_large_table() -> None:
    columns = [
        "A",
        "B",
        "C",
    ]
    data_frames = DataFrame("", index=np.arange(large_table_size), columns=columns)
    del data_frames


random_strings: list[str] = []


def create_random_strings() -> None:
    random_strings[:] = [str(i) for i in range(1000000, 1000000 + large_table_size)]


tables: dict[str, DataFrame] = {}


def create_string_table() -> None:
    columns = [
        "A",
        "B",
        "C",
    ]
    tables["df"] = DataFrame("", index=random_strings, columns=columns)


def create_set_from_strings() -> None:
    _ = set(random_strings)


def create_dict_from_strings() -> None:
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

# print("creating a random array ")  # noqa: ERA001  teaching: kept in the comment for the reader
# print("querying about 15mil entries by key")  # noqa: ERA001  teaching: kept in the comment for the reader


def more_stuff() -> None:
    size = 15000000
    random_words = [random_word(10) for _ in range(size)]
    df = tables["df"]
    print("after creation")
    print(type(random_words))
    print(len(random_words))
    print_data(df)
    df.iloc[0, 0] = "mark"
    df.iloc[0, 1] = "veltzer"

    print(df.to_numpy())
