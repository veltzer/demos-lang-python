#! /usr/bin/python

import mytimer
from multiprocessing import Process

# (a)
#############################################################
def stem_search(stems, stem_size):
    best_stem = ""
    best_count = 0

    for (stem,count) in stems.items():
       if stem_size == len(stem) and count > best_count:
           best_stem  = stem
           best_count = count

    if best_stem:
        print ("Most popular stem of size", stem_size, "is:",
                best_stem, "(occurs", best_count, "times)")
    return

#############################################################
if __name__ == "__main__":
    mytimer.start_timer()
    stems = {}

    for row in open("words", "r"):
        for count in range(1, len(row)):
            stem = row[0:count]
            if stem in stems:
                stems[stem] += 1
            else:
                stems[stem] = 1
            #print ("stem:", stem, "value:<", stems[stem], ">")
       
    mytimer.end_timer('Load')        

    # Process the stems
    # Senarios:
    # a)   n worker processes
    # b)    2 worker processes 14 stem sizes each
    # c)    2 worker processes using a queue

    processes=[]
    mytimer.start_timer()
    n = 30

    for stem_size in range(2, n+1):
        proc = Process(target=stem_search, args=(stems, stem_size))
        proc.start()
        processes.append(proc)
    
    for proc in processes:
        proc.join()
                 
    mytimer.end_timer('Process')  


# a) Process     : 111.250 seconds
#   Single CPU: 65.89 seconds
