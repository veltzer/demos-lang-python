import sys


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


def create_queue_from_string(exp):
    q = Queue()
    for c in exp.split(" "):
        q.push(int(c))
    return q


def process(q):
    r = Queue()
    for i in range(q.len()):
        c = q.pop()
        if c < 0:
            r.push(c)
        else:
            q.push(c)
    while q.len():
        r.push(q.pop())
    return r


def main():
    q = create_queue_from_string(sys.argv[1])
    r = process(q)
    print(r.data)


main()
