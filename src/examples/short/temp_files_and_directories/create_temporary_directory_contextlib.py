"""
This example shows how to create a directory with the contextlib
library in such a way as to have the directory and all of it's context
destroyed automatically when you are done with it.

This destruction also happens in the case of an exception thrown.

References:
- https://stackoverflow.com/questions/3223604/how-to-create-a-temporary-directory-and-get-the-path-file-name-in-python
"""

import contextlib
import os
import shutil
import tempfile


@contextlib.contextmanager
def cd(new_dir, cleanup=lambda: None):
    prev_dir = os.getcwd()
    os.chdir(os.path.expanduser(new_dir))
    try:
        yield
    finally:
        os.chdir(prev_dir)
        cleanup()


@contextlib.contextmanager
def tempdir():
    dir_path = tempfile.mkdtemp()

    def cleanup():
        shutil.rmtree(dir_path)
    with cd(dir_path, cleanup):
        yield dir_path


with tempdir():
    shutil.copy("/etc/passwd", "passwd")
