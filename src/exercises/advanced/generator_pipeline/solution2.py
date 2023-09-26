def line_generator(filename):
    with open(filename, "rt") as stream:
        for line in stream:
            yield line

def line_splitter():
    for x in line_generator("soliloquy.txt"):
        parts = x.split(" ")
        for part in parts:
            yield part

def lowercase_generator():
    for x in line_splitter():
        yield x.lower()


def remove_empty_strings():
    for x in lowercase_generator():
        if x!="":
            yield x

def newline_remover():
    for x in remove_empty_strings():
        if x.endswith("\n"):
            yield x[:-1]
        else:
            yield x

def punctuation_remover():
    punctuation_signs=['.', ',', ':', '?', ';']
    for x in newline_remover():
        if x[-1] in punctuation_signs:
            yield x[:-1]
        else:
            yield x

def extension_remover():
    extensions=["ed", "ing", "ion"]
    for x in punctuation_remover():
        found = False
        for y in extensions:
            if x.endswith(y):
                found = True
                yield x[:-len(y)]
        if not found:
            yield x

for x in extension_remover():
    print(x)
