"""
This example shows how to create a temporary directory in python and
destroy it's content once you are done with it.

References:
- https://stackoverflow.com/questions/3223604/how-to-create-a-temporary-directory-and-get-the-path-file-name-in-python
"""

import tempfile
import shutil
import os.path

dirpath = tempfile.mkdtemp()
print("dirpath is [{}]".format(dirpath))
shutil.copy("/etc/passwd", os.path.join(dirpath, "passwd"))
shutil.rmtree(dirpath)
