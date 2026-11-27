"""
This is a classic thread creation example.
"""

import threading
from typing import Any

# this function was written with NO consideratiion of threading...


def func(data: Any) -> None:
    print(data)


t = threading.Thread(target=func, args=("Hello",))
t.start()
t.join()
