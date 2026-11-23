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
    #    reactor.stop()
    # instead we must do:
    if stop:
        # pylint: disable=no-member
        reactor.callFromThread(reactor.stop)  # pyrefly: ignore[missing-attribute]


# run method in thread
# pylint: disable=no-member
reactor.callInThread(a_silly_blocking_method, 10, True)
# pylint: disable=no-member
reactor.callInThread(a_silly_blocking_method, 5, False)
print("before suggestThreadPoolSize")
reactor.suggestThreadPoolSize(2)
time.sleep(10)
print("finished sleeping...")
reactor.run()
