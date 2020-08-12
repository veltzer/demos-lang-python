"""
This example shows how to create a directory with the contextlib
library in such a way as to have the directory and all of it's context
destroyed automatically when you are donw with it.

This destruction also happens in the case of an exception thrown.

References:
- https://stackoverflow.com/questions/3223604/how-to-create-a-temporary-directory-and-get-the-path-file-name-in-python
"""

import contextlib
import os
import shutil
import tempfile

@contextlib.contextmanager
def cd(newdir, cleanup=lambda: True):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)
        cleanup()

@contextlib.contextmanager
def tempdir():
    dirpath = tempfile.mkdtemp()
    def cleanup():
        shutil.rmtree(dirpath)
    with cd(dirpath, cleanup):
        yield dirpath

with tempdir():
    shutil.copy("/etc/passwd", "passwd")
