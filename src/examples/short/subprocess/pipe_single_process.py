"""
This example shows how to call popen and get the return text.
"""

import subprocess


def system_check_output(arg):
    """
    A function that runs a command in a shell,checks that it succeeded and returns the output of that command
    in case of success. In case of error it will throw an exception
    This is similar to python>=2.7 subprocess.check_output
    """
    with subprocess.Popen(arg, stdout=subprocess.PIPE) as pr:
        (output, _errors) = pr.communicate()
        status = pr.returncode
        if status:
            raise ValueError("error in executing", arg)
        return output


try:
    system_check_output(["non_exist", "--non_exist"])
except FileNotFoundError:
    print("yes, got exception")
print(system_check_output(["ls", "-l"]))
