"""
This example shows:
- how to open and print to /dev/tty
- how to print to standard streams.
- how to close standard streams
- writing to a closed stream
"""

import sys
from typing import Optional, IO

print('Hello from regular print')
print('Hello from sys.stdout', file=sys.stdout)
print('Hello from sys.stderr', file=sys.stderr)

sys.stdout.close()

with open('/dev/tty', 'w') as f:  # type: Optional[IO[str]]
    f.write('Hello from /dev/tty...\n')
    f.flush()
    print('Another hello from /dev/tty...', file=f)
    # these will cause an exception
    try:
        print('printing to stdout will cause an exception')
    except ValueError:
        print('yes, got exception from regular print function', file=f)
    try:
        print('printing to stdout will cause an exception', file=sys.stdout)
    except ValueError:
        print('yes, got exception from print function with file=sys.stdout', file=f)
