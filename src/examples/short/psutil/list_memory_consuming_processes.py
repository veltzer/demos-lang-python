#!/usr/bin/python3

import psutil

process_list = []
for proc in psutil.process_iter():
    virtual_memory = proc.memory_info().vms
    if virtual_memory > 500000:
        process_list.append((proc.pid, proc.name(), virtual_memory))

process_list.sort(key=lambda x: x[2])
for x in process_list:
    print(x[1])
