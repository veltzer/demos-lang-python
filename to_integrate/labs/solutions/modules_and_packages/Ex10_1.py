#! /usr/bin/python

import mytimer

#import mymodules.mytimer2 as mytimer
#import cProfile

#cProfile.run("mytimer.start_timer()", "start.prof")

mytimer.start_timer()
lines = 0
for row in open("words"):
    lines += 1
    
mytimer.end_timer()
print ("Number of lines:", lines)
