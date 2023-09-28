from code import our_function_to_test
import pytest
import time
import subprocess

@pytest.fixture()
def server():
    # setup - bring the server up
    proc = subprocess.Popen(["python", "server.py"]) 
    # give the process 2 seconds to set up
    time.sleep(60)
    yield "server"
    # teardown - bring the server down
    proc.kill()


class TestSomething:
    def test_server(self, server):
        our_function_to_test()
