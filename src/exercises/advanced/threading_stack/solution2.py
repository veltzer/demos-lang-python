# this example shows a synchronized stack which does not sleep
# on pop on empty stack...

import time
from threading import Thread, RLock

number_of_elements = 400


class Stack:
    def __init__(self):
        self.lock = RLock()
        self.data = []

    def push(self, number):
        self.lock.acquire()
        self.data.append(number)
        print(number, ' pushed to stack')
        self.lock.release()

    def pop(self):
        if len(self.data) == 0:
            return None
        self.lock.acquire()
        if len(self.data) == 0:
            self.lock.release()
            return None
        number = self.data.pop(len(self.data) - 1)
        print(number, ' popped from stack')
        self.lock.release()
        return number


class ProduceOrConsume(Thread):
    def __init__(self, stack, consume, number):
        Thread.__init__(self)
        self.stack = stack
        self.consume = consume
        self.number = number

    def run(self):
        if self.consume:
            for i in range(number_of_elements):
                number = self.stack.pop()
                while number is None:
                    number = self.stack.pop()
                    time.sleep(1.0 / (self.number + 1))
        else:
            for i in range(number_of_elements):
                self.stack.push(i)
                time.sleep(1.0 / (self.number + 1))


def main():
    stack = Stack()
    threads = []
    for i in range(6):
        threads.append(ProduceOrConsume(stack, i % 2 == 0, i))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


main()
