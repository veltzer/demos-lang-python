"""
This is an example of how to use concurrent.futures

Note that this feature only works on python>=3.2.

References:
- https://docs.python.org/3/library/concurrent.futures.html

TODO:
- show how to handle exceptions coming out of the processes.
"""

import concurrent.futures


def work(n: int):
    # raise ValueError("this is an error")  # noqa: ERA001  teaching: kept in the comment for the reader
    for _ in range(n):
        pass
    return n


def main() -> None:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for r in executor.map(work, [100000000] * 8):
            print(r)


if __name__ == "__main__":
    main()
