"""
Solution
"""

import textwrap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _io import TextIOWrapper
    from collections.abc import Iterable


def lines2paragraphs(lines: TextIOWrapper):
    """Group lines into paragraphs as lists of lines."""
    paragraph: list[str] = []
    for raw_line in lines:
        line = raw_line.strip()
        if line == "":
            yield paragraph
            paragraph = []
        else:
            paragraph.append(line)
    # The last paragraph remains
    # (if the input didn"t end with an empty line)
    if len(paragraph) > 0:
        yield paragraph


def reformat(lines: Iterable[list[str]], chars: int):
    """
    Bonus: streaming lines->lines reformatter
    Generate lines of reformatted paragraphs.
    Paragraph in input and output are separated by empty lines.
    """
    for para in lines:
        yield from textwrap.wrap(" ".join(para), chars)
        yield ""


with open("/usr/share/doc/python/copyright") as f:
    mygen = reformat(lines2paragraphs(f), 50)
    for element in mygen:
        print(element)
