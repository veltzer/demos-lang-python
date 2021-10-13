"""
check which is faster, pandas with chunks or python with
no module.
"""

import gc
import gzip
import random
import time

import pandas


def time_it(f):
    def inner(*args, **kwargs):
        time1 = time.perf_counter()
        gc.disable()
        r = f(*args, **kwargs)
        gc.collect()
        time2 = time.perf_counter()
        print(time2 - time1, f.__name__)
        return r

    return inner


@time_it
def prepare_large_tsv_file(input_file: str, size: int):
    with gzip.open(input_file, "wt") as output_handle:
        for i in range(size):
            output_handle.write("\t".join([
                str(random.random()),
                str(random.random()),
                str(random.random()),
                str(random.random()),
            ]) + "\n")


@time_it
def read_it_with_pandas(input_file: str, separator: str):
    df = pandas.read_csv(
        input_file,
        sep=separator,
        header=None,
        # dtype="str",
    )
    return df.shape[0]


@time_it
def read_it_with_pandas_chunks(input_file: str, separator: str):
    reader = pandas.read_csv(
        input_file,
        sep=separator,
        chunksize=10000,
        header=None,
        # dtype="str",
    )
    line_count = 0
    for chunk in reader:
        line_count += chunk.shape[0]
    return line_count


@time_it
def read_it_with_python(input_file: str, separator: str):
    line_count = 0
    for line in open(input_file, "rt"):
        _ = line.split(separator)
        line_count += 1
    return line_count


@time_it
def read_it_with_python_gzip(input_file: str, separator: str):
    line_count = 0
    for line in gzip.open(input_file, "rt"):
        _ = line.split(separator)
        line_count += 1
    return line_count


@time_it
def loop_with_python(_input_file: str, _separator: str):
    for i in range(1000000):
        if i == 2:
            pass


def main():
    input_file = "/tmp/large.tsv"
    # size = 1000000
    # prepare_large_tsv_file(input_file, size)
    lc1 = read_it_with_python(input_file, "\t")
    lc2 = read_it_with_pandas(input_file, "\t")
    lc3 = read_it_with_pandas_chunks(input_file, "\t")
    lc4 = loop_with_python(input_file, "\t")
    assert lc1 == lc2
    assert lc2 == lc3
    assert lc3 == lc4


if __name__ == '__main__':
    main()
