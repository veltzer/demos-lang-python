#! /usr/bin/python

"""
This user written module contains a simple mechanism for
timing operations from Python.  It contains two functions,
start_timer(), which must be called first to initialise the
present time, and end_timer() which calculates the elapsed
CPU time and displays it.

>>> start_timer()
>>> end_timer()
End time    : 0.000 seconds
"""
import os
start_time = None

########################################################
# TIMER FUNCTIONS
def start_timer():
    """
    The start_timer() function marks the start of 
    a timed interval, to be completed by end_timer().
    This function requires no parameters.
    """
    global start_time
    (utime, stime) = os.times()[0:2]
    start_time = utime + stime
    return

def end_timer(txt='End time'):
    """
    The end_timer() function completes a timed interval
    started by start_timer.  It prints an optional text
    message (default 'End time') followed by the CPU time
    used in seconds.
    This function has one optional parameter, the text to 
    be displayed.
    """
    (utime, stime) = os.times()[0:2]
    end_time = utime + stime
    print (f"{txt:<12}: {end_time - start_time:01.3f} seconds")
    return

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()


