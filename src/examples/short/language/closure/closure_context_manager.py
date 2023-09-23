"""
This is a basic closure example.
"""
from typing import List


def iterate_it(filename):
    with open(filename) as f:
        yield from f


def iter_through_files(filenames: List[str]):
    filename_list = []
    for filename in filenames:
        filename_list.append(iterate_it(filename))
    return filename_list


def main():
    iterators = iter_through_files(["/etc/passwd", "/etc/group"])
    for i in iterators:
        for j in i:
            print(j, end="")


if __name__ == "__main__":
    main()
