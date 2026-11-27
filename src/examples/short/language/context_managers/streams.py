"""
This example shows how with works for file streams
"""


def count_lines_in_file(filename: str) -> int:
    with open(filename) as stream:
        counter = 0
        for _ in stream:
            counter += 1
    return counter


def count_lines_in_file_2(filename: str) -> int:
    stream = open(filename)  # noqa: SIM115  teaching: demonstrating manual open and close without a context manager
    try:
        counter = 0
        for _ in stream:
            counter += 1
        return counter
    finally:
        stream.close()


print(count_lines_in_file("/etc/passwd"))
print(count_lines_in_file_2("/etc/passwd"))
