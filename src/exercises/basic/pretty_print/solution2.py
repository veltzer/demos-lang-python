columns = [['H', 'He', 'Li', 'Be'], ['Hidrogen', 'Helium',
                                     'Litium', 'Berilium'], ['1.008', '4.003', '6.941', '9.012']]


# Before printing, we must know the width for each column.


def max_len(lines):
    """Return the length of the longest string."""
    lengths = []
    for line in lines:
        lengths.append(len(line))
    return max(lengths)


widths = []
for column in columns:
    widths.append(max_len(column))

# The separator line always looks the same, so let's build it once:
separator_line = '+'
for w in widths:
    separator_line += '-' * w + '+'

# Now output separators alternating with text rows

print(separator_line)

# If you haven't seen this function(*args_list) syntax yet -
# it's the same as zip(columns[0], columns[1], columns[2])
# but would work for any number of columns.
for row in zip(*columns):
    line = '|'
    for text, width in zip(row, widths):
        line += text.ljust(width) + '|'
    print(line)
    print(separator_line)
