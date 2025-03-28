""" command_line_parsing.py """

import sys

if len(sys.argv) > 3:
    print("You must pass two numbers to this script!", file=sys.stderr)
    sys.exit(1)
if len(sys.argv) <= 1:
    a = b = 2
else:
    try:
        a = int(sys.argv[1])
    except ValueError:
        print("Your argument is not a legal number you moron!", file=sys.stderr)
        sys.exit(1)
    try:
        b = int(sys.argv[2])
    except ValueError:
        print("Your argument is not a legal number you moron!", file=sys.stderr)
        sys.exit(1)
print(a + b)
