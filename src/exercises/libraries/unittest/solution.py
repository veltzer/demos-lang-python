"""
Solution
"""

import glob
import os
import shutil
import tempfile
import unittest
from typing import ClassVar


class TestGlob(unittest.TestCase):
    fnames: ClassVar = ["foo.txt", "bar.txt", "baz.py"]

    def setUp(self):
        """Create some files in a temp dir."""
        self.dir = tempfile.mkdtemp()
        for fname in self.fnames:
            with open(self.absolute(fname), "w"):
                pass

    def absolute(self, fname):
        return os.path.join(self.dir, fname)

    def tearDown(self):
        """Delete the temp dir."""
        shutil.rmtree(self.dir)

    def assert_glob(self, pattern, fnames):
        assert sorted(glob.glob(pattern)) == sorted(fnames)

    def test_current_dir_glob(self):
        """Test globbing in current dir."""
        os.chdir(self.dir)
        self.assert_glob("ba?.*", ["bar.txt", "baz.py"])

    def test_absolute_glob(self):
        """Test globbing with full path."""
        self.assert_glob(self.absolute("*xt"), map(
            self.absolute, ["foo.txt", "bar.txt"]))


unittest.main()
