"""
this is a program to check the python garbage collector.
"""

import signal

# watch "ps -e -o pid,cmd,%mem,rss,vsz | grep python | grep test"

a = [1, 2, 3] * 10000000
input("press any key...")
del a
while True:
    signal.pause()
