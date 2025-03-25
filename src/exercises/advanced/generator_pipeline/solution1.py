"""
solution1.py
"""


def line_generator(filename):
    with open(filename, "rt") as stream:
        yield from stream


def line_splitter():
    for x in line_generator("soliloquy.txt"):
        yield from x.split(" ")


def lowercase_generator():
    for x in line_splitter():
        yield x.lower()


def remove_empty_strings():
    for x in lowercase_generator():
        if x != "":
            yield x


def newline_remover():
    for x in remove_empty_strings():
        if x.endswith("\n"):
            yield x[:-1]


for t in newline_remover():
    print(t)
