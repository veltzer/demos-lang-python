"""
Compare speed of loading a large dict via json and pickle.

Results:
- in python2 json is much faster (this is opposite to python3).
"""

import timeit
import os
import json
import pickle
import tempfile
import random
import codecs

# first lets create a large dictionary and save it as json and pickle
d = {}
for x in range(100000):
    d[x] = [random.random() for _ in range(10)]

filename_json = tempfile.mktemp()
filename_pickle = tempfile.mktemp()

with codecs.open(filename_json, "wt", encoding="utf-8") as fp:
    json.dump(d, fp)
with open(filename_pickle, "wb") as fp:
    pickle.dump(d, fp, protocol=pickle.HIGHEST_PROTOCOL)


def load_json():
    with codecs.open(filename_json, "rt", encoding="utf-8") as fp:
        _ = json.load(fp)


def load_pickle():
    with open(filename_pickle, "rb") as fp:
        _ = pickle.load(fp)


repetitions = 10
print("json time {:.04f}".format(timeit.timeit(load_json, number=repetitions)))
print("pickle time {:.04f}".format(timeit.timeit(load_pickle, number=repetitions)))

length_json = os.stat(filename_json).st_size
length_pickle = os.stat(filename_pickle).st_size

print("json filesize {}".format(length_json))
print("pickle filesize {}".format(length_pickle))

os.unlink(filename_json)
os.unlink(filename_pickle)
