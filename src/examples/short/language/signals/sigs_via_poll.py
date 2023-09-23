"""
Example of how to receive signals synchronously via select and signal.set_wakeup_fd
This is copy of the referenced example which underwent heavy massaging.

Notes:
- this example works both in python 2 and 3.

TODO:
- When we get a signal in this example we still do not know what the signal is.

References:
http://www.pocketnix.org/doc/Fighting_set__wakeup__fd/
"""

import errno
import fcntl
import os
import select
import signal


def do_poll(poller):
    """
        We need this functions since python, unlike glibc, does not restart system
        calls.
        This means that when a signal arrives the poll system call will be broken,
        signal handler called by the system call not restarted. This means that the
        signal handler will work, will write the single byte to the pipe, but we will
        not be woken up by poll and instead, as is in python, an IOError will fly
        out with errno=EINTR.
        To overcome this we need a restartable poll
    """
    while True:
        try:
            return poller.poll()
        except IOError as e:
            if e.errno != errno.EINTR:
                raise


def main():
    # create a non blocking pipe
    pipe_r, pipe_w = os.pipe()
    flags = fcntl.fcntl(pipe_w, fcntl.F_GETFL, 0)
    flags = flags | os.O_NONBLOCK
    flags = fcntl.fcntl(pipe_w, fcntl.F_SETFL, flags)

    # set the write end of the pipe as the target of signals
    signal.set_wakeup_fd(pipe_w)

    # write a signal handler for our signal, otherwise we will
    # exit every time the signal is received...
    signal.signal(signal.SIGUSR1, lambda x, y: None)

    # pylint: disable=no-member
    poller = select.epoll()
    poller.register(pipe_r, select.EPOLLIN)

    print("mail loop staring...")
    # print("press CTRL+C to see how I catch the signal...")
    print(f"signal me with [kill -s SIGUSR1 {os.getpid()}]")
    while True:
        events = do_poll(poller)
        for _ in events:
            print("we got a signal")
            os.read(pipe_r, 1)


if __name__ == "__main__":
    main()
