"""
solution3.py
"""

from typing import Any


def line_generator():
    with open("soliloquy.txt") as stream:
        yield from stream


def line_splitter(g: Any):
    for x in g:
        yield from x.split(" ")


def lowercase_generator(g: Any):
    for x in g:
        yield x.lower()


def remove_empty_strings(g: Any):
    for x in g:
        if x != "":
            yield x


def newline_remover(g: Any):
    for x in g:
        if x.endswith("\n"):
            yield x[:-1]
        else:
            yield x


def punctuation_remover(g: Any):
    punctuation_signs = [".", ",", ":", "?", ";"]
    for x in g:
        if x[-1] in punctuation_signs:
            yield x[:-1]
        else:
            yield x


def extension_remover(g: Any):
    extensions = ["ed", "ing", "ion"]
    for x in g:
        found = False
        for y in extensions:
            if x.endswith(y):
                found = True
                yield x[:-len(y)]
        if not found:
            yield x


def main() -> None:
    list_generators = []
    list_of_all_geneators = [
        line_splitter,
        lowercase_generator,
        remove_empty_strings,
        newline_remover,
        punctuation_remover,
        extension_remover,
    ]
    while True:
        print("please add a generator out of the following list, -1 to end: ")
        for i, x in enumerate(list_of_all_geneators):
            print(i, x)
        selection = int(input())
        if selection == -1:
            break
        list_generators.append(list_of_all_geneators[selection])
    g = line_generator()
    for x in list_generators:
        g = x(g)
    for u in g:
        print(u)


if __name__ == "__main__":
    main()
