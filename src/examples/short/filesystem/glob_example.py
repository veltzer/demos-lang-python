"""
An example showing how to quickly iterate all the files
in a directory.
"""

import glob

for file in glob.glob('/etc/*'):
    print(file)
