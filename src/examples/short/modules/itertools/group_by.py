"""
This is a demo of itertools.groupby
"""

import itertools


def indentation(line):
    return len(line) - len(line.lstrip())


def main():
    data = """this is no indent 1
    this is no indent 2
        this is 1 indent 1
        this is 1 indent 2
    this is no indent 3
    this is no indent 4
        this is 1 indent 3
        this is 1 indent 4"""

    lines = data.split("\n")
    # lines.sort(key=indentation)
    # print(lines)
    # import sys
    # sys.exit(1)
    for indent, paragraph in itertools.groupby(lines , key=indentation):
        print(f"{indent}-spaced paragraph")
        for line in paragraph:
            print(line.strip())


main()
