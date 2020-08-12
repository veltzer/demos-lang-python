"""
this is how to disable tqdm
"""

import time

import tqdm

for i in tqdm.tqdm(range(1000), disable=True):
    time.sleep(1)
