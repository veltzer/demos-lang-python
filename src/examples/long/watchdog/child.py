"""
This is the child process, it randomizes how long to sleep
and then in 50% of the cases it dies wrongfully and in 50%
of the cases it dies with an OK exit code.
"""

import random
import time

t = random.randrange(2,5)
print(f"child sleeping for {t} seconds...")
time.sleep(t)
if random.random() < 0.5:
    raise ValueError("this is an error")
