#!/usr/bin/env python3

def yield_some_stuff():
    for t in range(5, 25, 5):
        yield t



for i in yield_some_stuff():
    print(i)
