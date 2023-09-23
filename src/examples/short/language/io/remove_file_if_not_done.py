"""
This is an example of how to remove a file if the work on it is not done.
The assumption is that the work on the file is done with a "with" block.

The thing to note here is that Exception stands for all exceptions EXCEPT
KeyboardInterrupt and SystemError which needs to be caught also.

References:
- https://stackoverflow.com/questions/4990718/how-can-i-write-a-try-except-block-that-catches-all-exceptions
"""

import os.path
import os
import time

filename = "/tmp/test"
if os.path.isfile(filename):
    os.unlink(filename)
try:
    with open(filename, "wb") as file_handle:
        for i in range(10):
            time.sleep(1)
            print(f"writing line {i}...")
            file_handle.write(f"line {i}\n".encode())
            file_handle.flush()
except (Exception, KeyboardInterrupt, SystemError) as e:
    print("unliking...")
    os.unlink(filename)
    raise e
