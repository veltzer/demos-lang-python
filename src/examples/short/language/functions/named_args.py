"""
This is a simple example of a function with named arguments
"""

import time


def function(times: int = 5, s: str = "mark", sleep_time: int = 4) -> None:
    for _ in range(times):
        print(s)
        time.sleep(sleep_time)


function(s="doron")
