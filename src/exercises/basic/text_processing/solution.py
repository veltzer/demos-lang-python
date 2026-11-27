"""
solution
"""


def right_align_to(lines: list[str], width: int):
    """Right-align all lines to given width."""
    return [line.rjust(width) for line in lines]


def max_len(lines: list[str]) -> int:
    """Return the length of the longest string."""
    lengths = [len(line) for line in lines]
    return max(lengths)


def right_align_to_longest(lines: list[str]):
    """Right-align all lines to the longest."""
    return right_align_to(lines, max_len(lines))


def main() -> None:
    """ main function """
    for line in right_align_to_longest(["foo", "x", "12345678"]):
        print(line)


main()
