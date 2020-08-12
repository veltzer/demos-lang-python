"""
This is a simple process that can output to any of three destinations:
- stdout
- stderr
- tty

The idea is for this program to be a test of how we can capture this output.

Examples:
[process] stdout
will log to stdout
[process] stderr
will log to stderr
[process] tty
will log to tty

and you can combine...
"""

import sys
import time
from typing import Optional, IO

args = sys.argv[1:]
if 'stdout' in args:
    print('this is stdout')
    for i in ['this ', 'is ', 'stdout\n']:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(1)

if 'stderr' in args:
    print('this is stderr', file=sys.stderr)
    for i in ['this ', 'is ', 'stderr\n']:
        print(i, end='', file=sys.stderr)
        sys.stderr.flush()
        time.sleep(1)

if 'tty' in args:
    f = open('/dev/tty', 'w')  # type: Optional[IO[str]]
    f.write('this is /dev/tty\n')
    for i in ['this ', 'is ', '/dev/tty\n']:
        print(i, end='', file=f)
        f.flush()
        time.sleep(1)
    f.close()

sys.exit(7)
