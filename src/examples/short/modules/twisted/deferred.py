"""
A more complex example involving defers.
"""

import time

from twisted.internet import defer

TARGET = 10000


def largeFibonnaciNumber():
    # create a Deferred object to return:
    d = defer.Deferred()

    # calculate the ten thousandth Fibonnaci number
    first = 0
    second = 1
    for i in range(TARGET - 1):
        new = first + second
        first = second
        second = new
        if i % 1000 == 0:
            print(f"Progress: calculating the {i}th Fibonnaci number")
    # give the Deferred the answer to pass to the callbacks:
    d.callback(second)
    # return the Deferred with the answer:
    return d


def printNumber(number):
    print(f"The {TARGET}th Fibonacci number is {number}")


def main():
    time_before = time.time()

    # call the function and get our Deferred
    d = largeFibonnaciNumber()

    time_after = time.time()

    print(f"Total time taken for largeFibonnaciNumber call: {time_after-time_before:.3f} seconds")

    # add a callback to it to output the number
    print("Adding the callback now.")
    d.addCallback(printNumber)


if __name__ == "__main__":
    main()
