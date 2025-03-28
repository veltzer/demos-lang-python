""" first solution """


class Queue:
    """
    Simple queue FIFO implementation using a python list
    """

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop(0)

    def len(self):
        return len(self.data)


q = Queue()
q.push(1)
q.push(2)
q.push(3)
assert q.pop() == 1
assert q.pop() == 2
assert q.pop() == 3
