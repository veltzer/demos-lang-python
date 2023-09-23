"""
This is a basic example of how to use tqdm.

References:
- https://pypi.python.org/pypi/tqdm
"""

import time

import tqdm

for i in tqdm.tqdm(range(1000), desc="some job"):
    time.sleep(1)
