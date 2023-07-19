"""
This is an example of a simple stream in Python
"""

import io


def count_lines(s: io.IOBase) -> int:
    count = 0
    for _ in s:
        count += 1
    return count


with open("/etc/passwd") as stream:
    print(type(stream))
    c = count_lines(stream)
    print(f"number of lines in file is {c}")
