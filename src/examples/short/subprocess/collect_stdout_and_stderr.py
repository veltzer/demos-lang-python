"""
This example shows how to run a subprocess and collect both its standard
output and his standard error.

References:
- https://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call/21000308
"""

import subprocess


def get_exitcode_stdout_stderr(args):
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    with subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        out, err = proc.communicate()
        exitcode = proc.returncode
        return exitcode, out, err


def main():
    exitcode, out, err = get_exitcode_stdout_stderr(["ls", "-l"])
    print(f"exitcode is [{exitcode}]")
    print(f"out is [{out.decode()}]")
    print(f"err is [{err.decode()}]")


main()
