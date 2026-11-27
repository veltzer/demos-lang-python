"""
This is a basic closure example.
"""


def iterate_it(filename: str):
    with open(filename) as f:
        yield from f


def iter_through_files(filenames: list[str]):
    return [iterate_it(filename) for filename in filenames]


def main() -> None:
    iterators = iter_through_files(["/etc/passwd", "/etc/group"])
    for i in iterators:
        for j in i:
            print(j, end="")


if __name__ == "__main__":
    main()
