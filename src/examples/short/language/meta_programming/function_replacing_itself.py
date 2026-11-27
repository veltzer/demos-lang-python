"""
This example shows a function that replaces itself at runtime: after a few
calls, `log` swaps itself in globals() for a cheaper no-op implementation,
so the check inside it no longer runs on subsequent calls.
"""

import itertools

counter = itertools.count(1)

def log_empty(_m) -> None:
    print("going through the cheap function")

def log(m: int) -> None:
    if next(counter) < 4:
        print(m)
    else:
        globals()["log"] = log_empty

for x in range(10):
    log(x)
