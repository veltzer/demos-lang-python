"""
solution1.py
"""

from threading import RLock, Thread


class Stack:
    def __init__(self):
        self.lock = RLock()
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


class Producer(Thread):
    def __init__(self, stack):
        Thread.__init__(self)
        self.stack = stack

    def run(self):
        for i in range(20):
            self.stack.push(i)


class Consumer(Thread):
    def __init__(self, stack):
        Thread.__init__(self)
        self.stack = stack

    def run(self):
        for _ in range(20):
            number = self.stack.pop()
            while number is None:
                number = self.stack.pop()


def main():
    stack = Stack()
    threads = []
    for _ in range(3):
        threads.append(Producer(stack))
    for _ in range(3):
        threads.append(Consumer(stack))
    for thread in threads:
        thread.start()


main()
