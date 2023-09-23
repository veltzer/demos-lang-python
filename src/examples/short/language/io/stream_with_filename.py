"""
This is an example of a simple stream in Python
"""


def count_lines(filename: str) -> int:
    with open(filename) as stream:
        count = 0
        for _ in stream:
            count += 1
        return count


c = count_lines("/etc/passwd")
print(f"number of lines in file is {c}")
