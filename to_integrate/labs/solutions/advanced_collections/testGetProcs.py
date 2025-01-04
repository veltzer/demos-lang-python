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

pids = {pid:value for pid, *value in igetprocs()}
print(pids)
       
