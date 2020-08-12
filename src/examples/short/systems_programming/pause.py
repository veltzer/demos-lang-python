"""
This example demonstrates the use of signal.pause().
If you already know about UNIX signals then this is no great surprise.
For those of you who do not know about UNIX signals,pause allows you
to do a busy wait without a busy wait. Pause will put your process
to sleep until any signal arrives. Since number of signals is small
this means that your process will be asleep most of the time. This
pattern allow you to react to signals in your 'main' thread since
the signal handler can change some variable and cause your main
thread to react,just as in this example.

Another thing to note is that when the signal handler is running it is running
in the context of the main thead and the threading module reports it as such.
This is typical UNIX behaviour.
"""

import os
import signal
import threading


# a small debugging function that prints the thread doing the printing...


def debug(msg):
    print(threading.currentThread().name, msg)


# a wrapper function to call an old signal handler


def call_old(old_val, signum, frame):
    if old_val is not None and old_val != signal.SIG_IGN and old_val != signal.SIG_DFL:
        old_val(signum, frame)


# this is my signal handler


def myhandler(signum, frame):
    debug('signalhandler: got signal {0}'.format(signum))
    if signum == signal.SIGUSR1:
        # lets call the old signal handler
        global oldsigusr1
        call_old(oldsigusr1, signum, frame)
        debug('signalhandler: doing some work')
    if signum == signal.SIGUSR2:
        # lets call the old signal handler
        global oldsigusr2
        call_old(oldsigusr2, signum, frame)
        # lets signal the main thread to stop
        debug('signalhandler: setting stop to True')
        global stop
        stop = True
    if signum == signal.SIGINT:
        # here we do not call the old function
        debug('signalhandler: dont press CTRL+C. Kill me using SIGUSR2')


oldsigusr1 = signal.getsignal(signal.SIGUSR1)
oldsigusr2 = signal.getsignal(signal.SIGUSR2)
oldsigint = signal.getsignal(signal.SIGINT)
stop = False
signal.signal(signal.SIGUSR1, myhandler)
signal.signal(signal.SIGUSR2, myhandler)
signal.signal(signal.SIGINT, myhandler)

debug(
    'mainthread: program starting,signal me using [kill -s SIGUSR1 {0}] or [kill -s SIGUSR2 {0}]'.format(os.getpid()))
while True:
    debug('mainthread: going to pause()')
    signal.pause()
    if stop:
        debug('mainthread: I was asked to stop')
        break
debug('mainthread: program ending')
