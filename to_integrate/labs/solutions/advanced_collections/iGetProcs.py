#! /usr/bin/python

import getprocs

   
###################################################################

def igetprocs():
    
    retn = getprocs.getfirstproc()
    yield retn
    
    while retn:
        retn = getprocs.getnextproc()
        if retn:
            yield retn

###################################################################

for proc in igetprocs():
    print(proc)
