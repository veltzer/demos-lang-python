"""
This is an example of how to catch CTRL+C in python

Notes:
- by catching the ctrl+C exception we can effectively
block the SIGINT signal. There are other ways to do
this ofcourse.
"""

import time

while True:
    try:
        time.sleep(2)
    except KeyboardInterrupt:
        print("got ctrl+c")
