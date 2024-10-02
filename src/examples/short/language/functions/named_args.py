"""
This is a simple example of a function with named arguments
"""

import time


def function(times=5, s="mark", sleep_time=4):
    for _ in range(times):
        print(s)
        time.sleep(sleep_time)


function(s="doron")
