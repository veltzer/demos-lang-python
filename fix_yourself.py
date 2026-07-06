#!/usr/bin/env python

counter = 0

def log_empty(m):
    print("going through the cheap function")

def log(m):
    global counter
    counter = counter + 1
    if counter < 4:
        print(m)
    else:
        globals()["log"] = log_empty

for x in range(10):
    log(x)
