"""
This example shows how to create two processes in python that communicate via a pipe.
"""

import subprocess


def system_pipe(list1, list2):
    """
    This function receives two lists to serve as the new processes
    """
    with subprocess.Popen(
        list1,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as pr1:
        with subprocess.Popen(
            list2,
            stdin=pr1.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ) as pr2:
            # the order of the following two lines don't matter but we do need
            # to wait for the two processes to be over...
            status = pr1.wait()
            (s_output2, s_error2) = pr2.communicate()
            if status:
                raise ValueError('error in executing', list1)
            status = pr2.returncode
            if status:
                raise ValueError('error in executing', list2, s_error2)
            return s_output2, s_error2


def main():
    try:
        # test error in first command
        print(system_pipe(
            ['ls', '-l', 'foo'],
            ['wc', '-l'],
        ))
    except ValueError as e:
        print('ok, got error for first command', e)
    try:
        # test error in second command
        print(system_pipe(
            ['ls', '-l'],
            ['wc', '-l', '--this_flag_doesnt_exist'],
        ))
    except ValueError as e:
        print('ok, got error for second command', e)
    # test output
    print(system_pipe(
        ['ls', '-l'],
        ['wc', '-l'],
    ))


main()
