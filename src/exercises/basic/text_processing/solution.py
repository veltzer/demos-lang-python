"""
solution
"""


def right_align_to(lines, width):
    """Right-align all lines to given width."""
    result = []
    for line in lines:
        result.append(line.rjust(width))
    return result


def max_len(lines):
    """Return the length of the longest string."""
    lengths = []
    for line in lines:
        lengths.append(len(line))
    return max(lengths)


def right_align_to_longest(lines):
    """Right-align all lines to the longest."""
    return right_align_to(lines, max_len(lines))


def main():
    """ main function """
    for line in right_align_to_longest(['foo', 'x', '12345678']):
        print(line)


main()
