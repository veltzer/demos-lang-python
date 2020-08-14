"""
This is an example of how to use concurrent.futures

Note that this feature only works on python>=3.2.

References:
- https://docs.python.org/3/library/concurrent.futures.html

TODO:
- show how to handle exceptions coming out of the processes.
"""

import concurrent.futures


def work(n):
    # raise ValueError("this is an error")
    for i in range(n):
        pass
    return i


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for r in executor.map(work, [100000000] * 8):
            print(r)


if __name__ == '__main__':
    main()
