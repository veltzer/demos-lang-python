"""
This example captures all output of a process: stdout, stderr and tty.

References:
http://stackoverflow.com/questions/11495783/redirect-subprocess-stderr-to-stdout
"""

import os
import pty
import sys

if len(sys.argv) < 2:
    print(f"{sys.argv[0]}: must supply process to run and arguments for it", file=sys.stderr)
    print(f"{sys.argv[0]}: use it like this:", file=sys.stderr)
    print(f"{sys.argv[0]}: {sys.argv[0]} ./write_to_any.py stdout stderr tty", file=sys.stderr)
    sys.exit(1)

pid, fd = pty.fork()
if pid == 0:
    os.execv(sys.argv[1], sys.argv[1:])
    print("execv didnt work", file=sys.stderr)
else:
    '''
    At the end of the loop we get an exception when the connection with the other side terminates.
    This is kinda ugly since strictly speaking this is not an error, but oh well.
    '''
    try:
        for line in os.fdopen(fd):
            print(f"got line [{line}]")
    except OSError as e:
        # print(e)
        pass
    pid, ret = os.wait()
    if os.WIFEXITED(ret):
        print(f"proc exited and status was [{os.WEXITSTATUS(ret)}]")
    if os.WIFSTOPPED(ret):
        print(f"proc stopped and stopsig was [{os.WSTOPSIG(ret)}]")
    if os.WIFSIGNALED(ret):
        print(f"proc signaled and signal was [{os.WTERMSIG(ret)}]")
