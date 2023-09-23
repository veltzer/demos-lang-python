"""
An example of how to use python3-progressbar

NOTES:
- maxval is 100 by default.
- calling pbar.update() (with no value) does nothing. you must pass a value.
"""

import time

import progressbar

pbar = progressbar.ProgressBar(maxval=10)
pbar.start()
for i in range(10):
    # do something
    time.sleep(1)
    # pbar.update(i+1)
    pbar.update(pbar.currval + 1)
pbar.finish()
