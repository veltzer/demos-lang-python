You are given the "process.py" process which emits lots of data but also a password somewhere.

You need to use the subprocess python module to run this process and process it's output.
Do not save all of it's output to a file and analyze the file post process.
Instead create a pipe and stream the data from the child process to the parent.
