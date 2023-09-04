"""
solution to the substring exercise
"""

import sys


def substring(string1, string2):
    """ substring implemenetation """
    if len(string2) < len(string1):
        return False
    for i in range(len(string2) - len(string1) + 1):
        k = 0
        while k < len(string1):
            if string1[k] != string2[i + k]:
                break
            k += 1
        else:
            return True
    return False


if len(sys.argv) != 3:
    print("You should pass exactly 2 strings to this program", file=sys.stderr)
    sys.exit(1)

print(substring(sys.argv[1], sys.argv[2]))
