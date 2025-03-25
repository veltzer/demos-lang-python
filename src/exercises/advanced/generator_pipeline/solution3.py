"""
solution3.py
"""

def line_generator():
    with open("soliloquy.txt", "rt") as stream:
        yield from stream


def line_splitter(g):
    for x in g:
        yield from x.split(" ")


def lowercase_generator(g):
    for x in g:
        yield x.lower()


def remove_empty_strings(g):
    for x in g:
        if x != "":
            yield x


def newline_remover(g):
    for x in g:
        if x.endswith("\n"):
            yield x[:-1]
        else:
            yield x


def punctuation_remover(g):
    punctuation_signs = [".", ",", ":", "?", ";"]
    for x in g:
        if x[-1] in punctuation_signs:
            yield x[:-1]
        else:
            yield x


def extension_remover(g):
    extensions = ["ed", "ing", "ion"]
    for x in g:
        found = False
        for y in extensions:
            if x.endswith(y):
                found = True
                yield x[:-len(y)]
        if not found:
            yield x


def main():
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
