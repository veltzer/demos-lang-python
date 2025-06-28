#! /usr/bin/python
import sys
import mytimer

mytimer.start_timer()
lines = 0
try:
    for row in open("words"):
        lines += 1
except OSError as err: 
    print("Could not open:",
           err.filename, err.args[1],
           file=sys.stderr)           
    
print("Number of lines:", lines)

try:
    mytimer.end_timer()
except SystemError as err:
    print("end_timer error:", err, file=sys.stderr)

print("We are all done")
