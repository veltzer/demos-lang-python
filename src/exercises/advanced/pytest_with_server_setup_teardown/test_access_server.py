"""
test_access_server.py
"""

import subprocess
import sys
import time
from pathlib import Path

from our_code import our_function_to_test


class TestSomething:

    @classmethod
    def setup_class(cls):
        # setup - bring the server up
        # the server sits next to this file, wherever the tests are run from
        cls.proc = subprocess.Popen([sys.executable, Path(__file__).with_name("server.py")])
        # give the process 2 seconds to set up
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        cls.proc.kill()

    def test_server(self):
        our_function_to_test()
