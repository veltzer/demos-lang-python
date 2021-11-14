"""
This is an example of how to catch a signal in python...

This program intercepts the SIGTERM signal and refuses to die...
"""
import signal
import time

def signal_handler(_sig, _frame):
    print('You send me SIGTERM, I Refuse to die!')

signal.signal(signal.SIGTERM, signal_handler)

i=0
while True:
    print(f"[{i}] nag nag...")
    i=i+1
    time.sleep(1)
