"""
solution3.py

this example shows a synchronized stack which does not sleep
on pop on empty stack...
"""

import time
from threading import Condition, Thread
from typing import override

number_of_elements = 400


class Stack:
    def __init__(self):
        self.cv = Condition()
        self.data = []

    def push(self, number):
        self.cv.acquire()
        self.data.append(number)
        self.cv.notify_all()
        # print("size of stack is ", len(self.data))  # noqa: ERA001  teaching: kept in the comment for the reader
        self.cv.release()

    def pop(self):
        self.cv.acquire()
        count = 0
        while len(self.data) == 0:
            # print("going to deep sleep...", iter,
            # threading.currentThread().number)
            count += 1
            if count > 1:
                print("Bonanza!")
            self.cv.wait()
        # print("i"m waking up...")
        number = self.data.pop(len(self.data) - 1)
        # print("size of stack is ", len(self.data))  # noqa: ERA001  teaching: kept in the comment for the reader
        self.cv.release()
        return number


class ProduceOrConsume(Thread):
    def __init__(self, stack, consume, number):
        Thread.__init__(self)
        self.stack = stack
        self.consume = consume
        self.number = number

    @override
    def run(self):
        if self.consume:
            for _i in range(number_of_elements):
                pass
                # number = self.stack.pop()  # noqa: ERA001  teaching: kept in the comment for the reader
                # time.sleep(1.0/(self.number+1))  # noqa: ERA001  teaching: kept in the comment for the reader
        else:
            for i in range(number_of_elements):
                self.stack.push(i)
                time.sleep(4.0 * 1.0 / (self.number + 1))


def main():
    stack = Stack()
    threads = [ProduceOrConsume(stack, i % 2 == 0, i) for i in range(6)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


main()
