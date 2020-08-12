# this example shows a synchronized stack which does not sleep
# on pop on empty stack...

import threading
import time

numberOfElems = 400


class Stack:
    def __init__(self):
        self.cv = threading.Condition()
        self.data = []

    def push(self, number):
        self.cv.acquire()
        self.data.append(number)
        self.cv.notifyAll()
        # print('size of stack is ', len(self.data))
        self.cv.release()

    def pop(self):
        self.cv.acquire()
        iter = 0
        while len(self.data) == 0:
            # print('going to deep sleep...', iter,
            # threading.currentThread().number)
            iter += 1
            if iter > 1:
                print('Bonanza!')
            self.cv.wait()
        # print('i'm waking up...')
        number = self.data.pop(len(self.data) - 1)
        # print('size of stack is ', len(self.data))
        self.cv.release()
        return number


class ProduceOrConsume(threading.Thread):
    def __init__(self, stack, consume, number):
        threading.Thread.__init__(self)
        self.stack = stack
        self.consume = consume
        self.number = number

    def run(self):
        if self.consume:
            for i in range(numberOfElems):
                number = self.stack.pop()
                # time.sleep(1.0/(self.number+1))
        else:
            for i in range(numberOfElems):
                self.stack.push(i)
                time.sleep(4.0 * 1.0 / (self.number + 1))


stack = Stack()
threads = [None] * 6
for i in range(6):
    threads[i] = ProduceOrConsume(stack, i % 2 == 0, i)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
