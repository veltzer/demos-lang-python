#!/usr/bin/python3

import os
import sys
import os.path
import fcntl
import time

'''
This is an example of how to make sure only a single python process is
running of a specific kind...

References:
- http://stackoverflow.com/questions/220525/ensure-a-single-instance-of-an-application-in-linux
'''

do_fork = False


def single_runner():
    program_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    pid_file = '/tmp/{}.pid'.format(program_name)
    try:
        fp = os.open(pid_file, os.O_WRONLY | os.O_CREAT)
        fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        # another instance is running
        print('this program is already running...', file=sys.stderr)
        sys.exit(1)


# this does not work
def single_runner_simple():
    program_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    pid_file = '/tmp/{}.pid'.format(program_name)
    # if os.path.isfile(pid_file):
    #    os.unlink(pid_file)
    try:
        os.open(pid_file, os.O_CREAT | os.O_EXCL)
    except IOError as e:
        print(e)
        # another instance is running
        print('this program is already running...', file=sys.stderr)
        sys.exit(1)


single_runner()
while True:
    time.sleep(3600)
