"""
This example shows how to create a temporary directory in python and
destroy it's content once you are done with it.

References:
- https://stackoverflow.com/questions/3223604/how-to-create-a-temporary-directory-and-get-the-path-file-name-in-python
"""

import tempfile
import shutil
import os.path

dir_path = tempfile.mkdtemp()
print(f"dir_path is [{dir_path}]")
shutil.copy("/etc/passwd", os.path.join(dir_path, "passwd"))
shutil.rmtree(dir_path)
