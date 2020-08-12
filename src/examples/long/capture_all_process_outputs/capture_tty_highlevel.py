"""
This example captures all output of a process: stdout, stderr and tty.

References:
http://stackoverflow.com/questions/11495783/redirect-subprocess-stderr-to-stdout
"""

import os
import pty
import sys

if len(sys.argv) < 2:
    print('{0}: must supply process to run and arguments for it'.format(
        sys.argv[0]), file=sys.stderr)
    print('{0}: use it like this:'.format(sys.argv[0]))
    print('{0}: {0} ./write_to_any.py stdout stderr tty'.format(sys.argv[0]))
    sys.exit(1)

(pid, fd) = pty.fork()
if pid == 0:
    os.execv(sys.argv[1], sys.argv[1:])
    print('execv didnt work', file=sys.stderr)
else:
    '''
    At the end of the loop we get an exception when the connection with the other side terminates.
    This is kinda ugly since strictly speaking this is not an error, but oh well.
    '''
    try:
        for line in os.fdopen(fd):
            print('got line [{0}]'.format(line))
    except OSError as e:
        # print(e)
        pass
    (pid, ret) = os.wait()
    if os.WIFEXITED(ret):
        print('proc exited and status was [{}]'.format(os.WEXITSTATUS(ret)))
    if os.WIFSTOPPED(ret):
        print('proc stopped and stopsig was [{}]'.format(os.WSTOPSIG(ret)))
    if os.WIFSIGNALED(ret):
        print('proc signaled and signal was [{}]'.format(os.WTERMSIG(ret)))
