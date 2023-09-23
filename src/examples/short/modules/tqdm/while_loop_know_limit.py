"""
This is how to use tqdm when you know number of iterations.

Notes:
- in the first context manager method you must take care to update the progress
bar *on every piece of work you do* so that the progress bar will get to 100%
at the end of the work.

References:
- https://pypi.python.org/pypi/tqdm
"""

import random

import tqdm

limit = 100000000

# example with a context manager
counter = 0
with tqdm.tqdm(total=limit) as pbar:
    while True:
        r = random.randrange(0, 100)
        pbar.update(r)
        counter += r
        if counter > limit:
            break

# example of not updating correctly
with tqdm.tqdm(total=limit) as pbar:
    pbar.update(1000)
pbar.close()

# example without a context manager
pbar = tqdm.tqdm(total=limit)
counter = 0
while True:
    r = random.randrange(0, 100)
    pbar.update(r)
    counter += r
    if counter > limit:
        break
# you must add this to close
pbar.close()
