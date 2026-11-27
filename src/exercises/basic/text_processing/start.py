"""
solution
"""


def right_align_to(lines: list[str], width: int):
    """Right-align all lines to given width."""
    return [line.rjust(width) for line in lines]


def main() -> None:
    """ main function """
    for line in right_align_to(["foo", "x", "12345678"], 8):
        print(line)


main()
