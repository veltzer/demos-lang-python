"""
This example shows how to call popen and get the return text.
"""

import subprocess

'''
A function that runs a command in a shell,checks that it succeeded and returns the output of that command
in case of success. In case of error it will throw an exception
This is similar to python>=2.7 subprocess.check_output
'''


def system_check_output(arg):
    pr = subprocess.Popen(arg, stdout=subprocess.PIPE)
    (output, errout) = pr.communicate()
    status = pr.returncode
    if status:
        raise ValueError('error in executing', cmd)
    return output


try:
    system_check_output(['non_exist', '--non_exist'])
except:
    print('yes, got exception')
print(system_check_output(['ls', '-l']))
