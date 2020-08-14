"""
This example shows how to run a subprocess and collect both it's standard
output and his standard error.

References:
- https://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call/21000308
"""

import subprocess


def get_exitcode_stdout_stderr(args):
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    return exitcode, out, err


exitcode, out, err = get_exitcode_stdout_stderr(["ls", "-l"])
print("exitcode is [{}]".format(exitcode))
print("out is [{}]".format(out.decode()))
print("err is [{}]".format(err.decode()))
