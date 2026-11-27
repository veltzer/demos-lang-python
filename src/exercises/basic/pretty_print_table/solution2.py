"""
solution
"""


def max_len(lines: list[str]) -> int:
    """Return the length of the longest string."""
    lengths = [len(line) for line in lines]
    return max(lengths)


def main() -> None:
    """ main function """
    columns = [
        ["H", "He", "Li", "Be"],
        ["Hidrogen", "Helium", "Litium", "Berilium"],
        ["1.008", "4.003", "6.941", "9.012"],
    ]
    # Before printing, we must know the width for each column.
    widths = [max_len(column) for column in columns]

    # The separator line always looks the same, so let"s build it once:
    separator_line = "+"
    for width in widths:
        separator_line += "-" * width + "+"

    # Now output separators alternating with text rows

    print(separator_line)

    # If you havent seen this function(*args_list) syntax yet -
    # its the same as zip(columns[0], columns[1], columns[2])
    # but would work for any number of columns.
    for row in zip(*columns, strict=False):
        line = "|"
        for text, width in zip(row, widths, strict=False):
            line += text.ljust(width) + "|"
        print(line)
        print(separator_line)


main()
