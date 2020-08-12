"""
This example only does an os.execv
"""

import os
import sys

if len(sys.argv) < 2:
    print('{0}: must supply process to run and arguments for it'.format(
        sys.argv[0]), file=sys.stderr)
    print('{0}: use it like this:'.format(sys.argv[0]))
    print('{0}: {0} ./write_to_any.py stdout stderr tty'.format(sys.argv[0]))
    sys.exit(1)

os.execv(sys.argv[1], sys.argv[1:])
