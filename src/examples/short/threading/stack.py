"""
An example of a stack for multi threaded programming.
"""

import threading


class Stack:
    def __init__(self):
        self.lock = threading.RLock()
        self.numbers = []

    def push(self, number):
        with self.lock:
            self.numbers.append(number)
            print(f"{number} pushed to stack")

    def pop(self):
        with self.lock:
            if len(self.numbers) == 0:
                return None
            number = self.numbers.pop(len(self.numbers) - 1)
        print(f"{number} popped from stack")
        return number


class Producer(threading.Thread):
    def __init__(self, stack):
        threading.Thread.__init__(self)
        self.stack = stack

    def run(self):
        for i in range(20):
            self.stack.push(i)


class Consumer(threading.Thread):
    def __init__(self, stack):
        threading.Thread.__init__(self)
        self.stack = stack

    def run(self):
        for _ in range(20):
            number = self.stack.pop()
            while number is None:
                number = self.stack.pop()


def main():
    stack = Stack()
    threads = []
    print('starting')
    for _ in range(3):
        threads.append(Producer(stack))
        threads.append(Consumer(stack))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('ending')


main()
