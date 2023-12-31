"""
Compare speed of loading a large dict via json and pickle.

Results:
- pickle is much faster in python3 (the opposite of python2).
"""

import timeit
import os
import json
import pickle
import tempfile
import random


def load_json(filename_json):
    with open(filename_json, "rt") as f:
        json.load(f)


def load_pickle(filename_pickle):
    with open(filename_pickle, "rb") as f:
        pickle.load(f)


def main():
    # first lets create a large dictionary and save it as json and pickle
    d = {}
    for x in range(100000):
        d[x] = [random.random() for _ in range(10)]

    filename_json = tempfile.mktemp()
    filename_pickle = tempfile.mktemp()

    with open(filename_json, "wt") as fp:
        json.dump(d, fp)
    with open(filename_pickle, "wb") as fp:
        pickle.dump(d, fp, protocol=pickle.HIGHEST_PROTOCOL)
    repetitions = 10

    """
    def my_load_json():
        load_json(filename_json)
    json_time = timeit.timeit(my_load_json, number=repetitions)
    """

    json_time = timeit.timeit(lambda : load_json(filename_json), number=repetitions)
    print(f"json time {json_time:.04f}")
    pickle_time = timeit.timeit(lambda : load_pickle(filename_pickle), number=repetitions)
    print(f"pickle time {pickle_time:.04f}")

    length_json = os.stat(filename_json).st_size
    length_pickle = os.stat(filename_pickle).st_size

    print(f"json filesize {length_json}")
    print(f"pickle filesize {length_pickle}")

    os.unlink(filename_json)
    os.unlink(filename_pickle)

if __name__ == "__main__":
    main()
