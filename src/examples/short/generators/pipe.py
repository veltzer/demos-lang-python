"""
Example of generators using generators
"""


def list_input():
    counter = 0
    while True:
        yield counter
        counter += 1
        if counter == 10:
            break


def square_it(input_generator):
    for x in input_generator():
        yield x ** 2


def main():
    result = []
    for x in square_it(list_input):
        result.append(x + 1)
    print(result)


main()
