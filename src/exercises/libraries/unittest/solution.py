"""
Solution
"""

import glob
import os
import shutil
import tempfile
import unittest
from typing import ClassVar, override


class TestGlob(unittest.TestCase):
    fnames: ClassVar = ["foo.txt", "bar.txt", "baz.py"]

    @override
    def setUp(self) -> None:
        """Create some files in a temp dir."""
        self.dir = tempfile.mkdtemp()
        for fname in self.fnames:
            with open(self.absolute(fname), "w"):
                pass

    def absolute(self, fname: str) -> str:
        return os.path.join(self.dir, fname)

    @override
    def tearDown(self) -> None:
        """Delete the temp dir."""
        shutil.rmtree(self.dir)

    def assert_glob(self, pattern: str, fnames: list[str] | map[str]) -> None:
        assert sorted(glob.glob(pattern)) == sorted(fnames)

    def test_current_dir_glob(self) -> None:
        """Test globbing in current dir."""
        os.chdir(self.dir)
        self.assert_glob("ba?.*", ["bar.txt", "baz.py"])

    def test_absolute_glob(self) -> None:
        """Test globbing with full path."""
        self.assert_glob(self.absolute("*xt"), map(
            self.absolute, ["foo.txt", "bar.txt"]))


unittest.main()
