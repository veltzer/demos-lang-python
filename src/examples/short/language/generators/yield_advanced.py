"""
This is a time sharing example...
The main code of this example is like an operating system that shares time
between the two "threads" or "processes". Each one has a state,stack and all.
This is a co-operative system: if one of the processes never calls yield or goes
into a blocking call then the entire system stalls.
What is this good for?
Handling many pseudo clients in one thread in python. Just make sure you never do
IO in your code and just ask the "OS" (main code) using the return value of yield
to do the calls for you. The "OS" will return the data needed via the "next()" method.
This way you can handle thousands of connections in one python thread (this is actually
what happens with twisted).
"""


def evens():
    for x in range(0, 100, 2):
        print(f"evens say {x}")
        yield


def odds():
    for x in range(10001, 10101, 2):
        print(f"odds say {x}")
        yield


def main():
    c1 = evens()
    c1.__next__()
    c2 = odds()
    c2.__next__()
    for _ in range(10):
        c1.__next__()
    c2.__next__()


main()
