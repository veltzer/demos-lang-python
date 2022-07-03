"""
An example demonstrating twisted's 'callInThread' function.
"""

import time

from twisted.internet import reactor


def aSillyBlockingMethod(t, stop):
    print('starting...')
    time.sleep(t)
    print(t, 'seconds have passed')
    # this will not work as we are running in a separate thread...
    # if stop:
    #    reactor.stop()
    # instead we must do:
    if stop:
        # pylint: disable=no-member
        reactor.callFromThread(reactor.stop)


# run method in thread
# pylint: disable=no-member
reactor.callInThread(aSillyBlockingMethod, 10, True)  # type: ignore
# pylint: disable=no-member
reactor.callInThread(aSillyBlockingMethod, 5, False)  # type: ignore
print('before suggestThreadPoolSize')
reactor.suggestThreadPoolSize(2)  # type: ignore
time.sleep(10)
print('finished sleeping...')
reactor.run()  # type: ignore
