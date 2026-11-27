"""
grep implemented as three stacked generator expressions.
"""
import re
import sys


def _iter_lines(filenames: list[str]):
    for filename in filenames:
        with open(filename, encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                yield filename, lineno, line


def grep(pattern: str, filenames: list[str]):
    pat = re.compile(pattern)
    lines = (
        (filename, lineno, line)
        for filename, lineno, line in _iter_lines(filenames)
    )
    stripped = (
        (filename, lineno, line.rstrip("\n"))
        for filename, lineno, line in lines
    )
    return (
        (filename, lineno, text)
        for filename, lineno, text in stripped
        if pat.search(text)
    )


def main() -> None:
    pattern, *files = sys.argv[1:]
    for filename, lineno, text in grep(pattern, files):
        print(f"{filename}:{lineno}:{text}")


if __name__ == "__main__":
    main()
