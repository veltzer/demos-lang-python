""" generator_in_generator.py """


def give_me_little_data():
    yield "this is little data 1"
    yield "this is little data 2"


def give_me_more_data():
    yield "this is more data 1"
    yield "this is more data 2"


def give_me_some_data():
    yield from give_me_little_data()
    yield "this is data from the middle"
    yield from give_me_more_data()
    yield "this is data from the end"


def main():
    for x in give_me_some_data():
        print("outer loop", x)


main()
