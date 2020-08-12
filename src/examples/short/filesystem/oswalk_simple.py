"""
This is an example of the 'os.walk' API that allows one to traverse
a directory of files recursively.
This is used to implement find(1)+grep(1) in just a few lines of python.
If you just want to iterate files then you just need the first block
of code in the loop.
Notice that the root changes all the time.
Notice that the file names and directory names that you get are relative
to the root that you get and not to the root folder of the scan.
"""

import os
import sys

if len(sys.argv) < 2:
    raise ValueError('please pass root_folder')
root_folder = sys.argv[1]

for root, directories, files in os.walk(root_folder):
    for file in files:
        full = os.path.join(root, file)
        print('file [{}]'.format(full))
    for directory in directories:
        full = os.path.join(root, directory)
        print('folder [{}]'.format(full))
