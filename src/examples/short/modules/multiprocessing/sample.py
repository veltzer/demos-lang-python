"""
simple.py
"""

from multiprocessing import Process, Queue
from typing import Any


def f(m: Any) -> None:
    m.put([42, None, "hello"])


if __name__ == "__main__":
    q = Queue()  # type: Queue
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
