#!/usr/bin/env python3

import sys
import operator

if len(sys.argv) != 2:
    print("Please specify input file name", file=sys.stderr)
    sys.exit(1)

def get_second_item(t):
    return t[1]


filename = sys.argv[1]
words = dict()
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        for word in line.split(" "):
            if word not in words:
                words[word]=0
            words[word] += 1
l=list(words.items()) 
# l.sort(key=get_second_item, reverse=True)
l.sort(key=operator.itemgetter(1), reverse=True)
print(l[:3])
# print("\n".join(map(operator.itemgetter(0), l[:3])))
