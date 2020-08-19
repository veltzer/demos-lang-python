from threading import RLock, Thread


class Stack:
    def __init__(self):
        self.lock = RLock()
        self.numbers = []

    def push(self, number):
        self.lock.acquire()
        self.numbers.append(number)
        print(number, ' pushed to stack')
        self.lock.release()

    def pop(self):
        self.lock.acquire()
        if len(self.numbers) == 0:
            self.lock.release()
            return None
        number = self.numbers.pop(len(self.numbers) - 1)
        print(number, ' popped from stack')
        self.lock.release()
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
        for i in range(20):
            number = self.stack.pop()
            while number is None:
                number = self.stack.pop()


def main():
    stack = Stack()
    threads = []
    for i in range(3):
        threads.append(Producer(stack))
    for i in range(3):
        threads.append(Consumer(stack))
    for thread in threads:
        thread.start()


main()
