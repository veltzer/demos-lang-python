"""
solution.py
"""

import threading


class RWL:
    def __init__(self):
        self._writersWaiting = 0
        self._readersWaiting = 0
        self._writersInside = 0
        self._readersInside = 0
        self.c = threading.Condition()

    def reader_enter(self):
        with self.c:
            self._readersWaiting += 1
            while self._writersInside:
                self.c.wait()
            self._readersWaiting -= 1
            self._readersInside += 1

    def reader_leave(self):
        with self.c:
            self._readersInside -= 1
            # self.c.notifyAll()
            if self._readersInside == 0:
                self.c.notify()

    def writer_enter(self):
        with self.c:
            self._writersWaiting += 1
            while self._readersInside or self._writersInside:
                self.c.wait()
            self._writersWaiting -= 1
            self._writersInside += 1

    def writer_leave(self):
        with self.c:
            self._writersInside -= 1
            self.c.notify_all()
