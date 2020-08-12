"""
Example of timing python code using the 'time' module

Note that the time measured by time.time() is the wall
clock time which is not always what you want to measure.
"""

import time

time_before = time.time()
time.sleep(2)
time_after = time.time()
print('time taken: {0:.3f} seconds'.format(time_after - time_before))
