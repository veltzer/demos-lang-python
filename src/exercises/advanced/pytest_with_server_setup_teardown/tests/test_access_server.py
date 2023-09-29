import time
import subprocess

# pylint: disable=relative-beyond-top-level
from .code import our_function_to_test


class TestSomething:

    @classmethod
    def setup_class(cls):
        # setup - bring the server up
        # pylint: disable=consider-using-with
        cls.proc = subprocess.Popen(["python", "server.py"])
        # give the process 2 seconds to set up
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        cls.proc.kill()

    def test_server(self):
        our_function_to_test()
