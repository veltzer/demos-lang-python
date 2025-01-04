#!/usr/local/bin/python
import sys, glob, os, stat
import os.path

if sys.platform == 'win32':
    dirp = os.environ['HOMEPATH']
else:
    dirp = os.environ['HOME']

import re
for filename in glob.glob(os.path.join(dirp, '*')):
    size = os.stat(filename)[stat.ST_SIZE]
   
    if size > 0:
        filename = re.sub(r'.*\\', '', filename)
        print(filename, size, 'bytes')

print()
dirlen = len(dirp) + 1
for filename in glob.glob(os.path.join(dirp, '*')):
    size = os.stat(filename)[stat.ST_SIZE]
   
    if size > 0:
        print(filename[dirlen:], size, 'bytes')

print()
for filename in glob.glob(os.path.join(dirp, '*')):
    size = os.stat(filename)[stat.ST_SIZE]
   
    if size > 0:
        print(os.path.basename(filename), size, 'bytes')

