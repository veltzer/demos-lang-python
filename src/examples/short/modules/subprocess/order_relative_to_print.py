"""
Run this example once with a pipe and once without and see the different order of the output.

Can you explain why we see the print after the check_call?

Here is the explanation:
Python automatically sets the buffering method on stdout according to the type of file that
stdout is:
- if stdout is a pipe then the buffering is buffer length based.
- if stdout is a terminal then the buffering is end-of-line based.
This means that when you run this example on a regular terminal the "Hello, World!" will come out first
since it ends with a newline and only then the "Goodbye, World!".
If you run this example with a pipe then "Hello, World!" will remain in the buffer, "Goodbye, World!"
will be outputted and stdout will be flushed at the end of the program.

How can you solve these issues? Three solutions:
- configure stdout to be newline based at the beginning of the program
- always flush after prints
- always flush before subprocess.check_call, os.system etc...
"""

import subprocess

# the next few lines will cause the output to be consistent
# import sys  # noqa: ERA001  teaching: kept in the comment for the reader
# sys.stdout = open(
#   sys.stdout.fileno(),  # noqa: ERA001  teaching: kept in the comment for the reader
#   mode="w",  # noqa: ERA001  teaching: kept in the comment for the reader
#   buffering=1,  # noqa: ERA001  teaching: kept in the comment for the reader
#   encoding=sys.stdout.encoding,
#   errors=sys.stdout.errors,  # noqa: ERA001  teaching: kept in the comment for the reader
#   newline=sys.stdout.newlines,  # noqa: ERA001  teaching: kept in the comment for the reader
#   closefd=False  # noqa: ERA001  teaching: kept in the comment for the reader
# )  # noqa: ERA001  teaching: kept in the comment for the reader
print("Hello, World!")
subprocess.check_call(["echo", "Goodbye, World!"])
