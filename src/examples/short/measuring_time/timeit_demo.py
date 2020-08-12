"""
Example of timing python code using the 'timeit' module

Why should you use this module and not time everything yourself?
Well, if you time things yourself you must be very careful to:
- use process/thread time and not clock time
- turn off garbage collection so that it wont soil your measurements
and other pitfalls.
Frankly, timeit does not do any of the above...:)

Usage:
- you can some python code as string to the 'timeit' function.
This is, ofcourse, bad from both a security and performance perspectives.
- you can pass the name of a function which receives no arguments
which will be called by 'timeit'. This is security and performance wise.
- you can use the 'timeit' module from the command line like this:
python -m timeit -s 'text = "sample string"; char = "g"'  'char in text'
- the 'number' argument must be passed if you are measuring a function.
otherwise it will be the default 100000.

NOTES:
- from the 'mysleep' example we learn that timeit times wallclock
time and not cpu time.
- this means that when using 'timeit' you are exposed to the following
issues:
    - if the OS schedules other threads on the core you are on you
    will be measuring their time as well.
    - if you are doing IO or waits in your code, then you are measuring
    them as well.
    - if the OS is moving your process/thread between cores and that
    process takes time or makes your process/thread slower, you will
    be measuring that as well.
    - you will be measuring python garbage collection overhead as well.

How to measure CPU only functions using timeit?
just measure a few times and take the best time.
The IO and wait issues are avoiding by not having them in your code.
The other thread/process/garbage collector/OS CPU moving issues are avoided
by taking the best measurement.
"""

import time
import timeit


def my_sleep():
    time.sleep(2)

print(timeit.timeit('\'-\'.join(str(n) for n in range(100))', number=10000))
print(timeit.timeit(my_sleep, number=1))
print(timeit.timeit(my_sleep))
