"""
This example shows how to copy a file in python

This example is based on shutil.copyfileobj which shuffles
data from one file handle to another.
"""

import os
import shutil

source_file = "/etc/passwd"
target_file = "/tmp/passwd"

if os.path.isfile(target_file):
    os.unlink(target_file)
with open(source_file) as source_file_handle:
    with open(target_file, "w") as target_file_handle:
        shutil.copyfileobj(source_file_handle, target_file_handle)
