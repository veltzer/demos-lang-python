#!/usr/bin/env python3

import sys

def my_substring(s1, s2):
    if len(s2) < len(s1):
        return False
    for i in range(len(s2)-len(s1)):
        k = 0
        while k < len(s1):
            if s1[k] != s2[i+k]:
                break
            k += 1
        else:
            return True
    return False 

if len(sys.argv) != 3:
    print("You should pass exactly 2 strings to this program", file=sys.stderr)
    sys.exit(1)

print(my_substring(sys.argv[1], sys.argv[2]))
