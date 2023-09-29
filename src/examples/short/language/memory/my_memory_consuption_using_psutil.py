import os
import psutil


_big_list = [0] * 1000000
pid = os.getpid()
process = psutil.Process(pid)
memory_usage = process.memory_info().rss
print(f"memory_usage is {memory_usage}")
