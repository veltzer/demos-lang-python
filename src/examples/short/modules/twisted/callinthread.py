"""
An example demonstrating twisted"s "callInThread" function.
"""

import time

from twisted.internet import reactor


def a_silly_blocking_method(t, stop):
    print("starting...")
    time.sleep(t)
    print(t, "seconds have passed")
    # this will not work as we are running in a separate thread...
    # if stop:
    #    reactor.stop()  # noqa: ERA001  teaching: kept in the comment for the reader
    # instead we must do:
    if stop:
        reactor.callFromThread(reactor.stop)


# run method in thread
reactor.callInThread(a_silly_blocking_method, 10, stop=True)
reactor.callInThread(a_silly_blocking_method, 5, stop=False)
print("before suggestThreadPoolSize")
reactor.suggestThreadPoolSize(2)
time.sleep(10)
print("finished sleeping...")
reactor.run()
