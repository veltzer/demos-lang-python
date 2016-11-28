#!/usr/bin/python3

"""
This example shows:
- how to open and print to /dev/tty
- how to print to standard streams.
- how to close standard streams
- writing to a closed stream
"""

import sys  # for stdout, stderr

print('Hello from regular print')
print('Hello from sys.stdout', file=sys.stdout)
print('Hello from sys.stderr', file=sys.stderr)

sys.stdout.close()

with open('/dev/tty', 'w') as f:
    f.write('Hello from /dev/tty...\n')
    f.flush()
    print('Another hello from /dev/tty...', file=f)
    # these will cause an exception
    try:
        print('printing to stdout will cause an exception')
    except:
        print('yes, got exception from regular print function', file=f)
    try:
        print('printing to stdout will cause an exception', file=sys.stdout)
    except:
        print('yes, got exception from print functino with file=sys.stdout', file=f)
