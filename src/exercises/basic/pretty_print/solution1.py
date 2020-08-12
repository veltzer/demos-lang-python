columns = [['H', 'He', 'Li', 'Be'], ['Hidrogen', 'Helium',
                                     'Litium', 'Berilium'], ['1.008', '4.003', '6.941', '9.012']]

# The separator line always looks the same, so let's build it once:
separator_line = '+'
for column in columns:
    separator_line += '-' * 10 + '+'

# Now output separators alternating with text rows

print(separator_line)

# A better way to write it would be: zip(*columns)
# but you probably haven't seen that syntax yet.
for row in zip(columns[0], columns[1], columns[2]):
    line = '|'
    for text in row:
        line += text.ljust(10) + '|'
    print(line)
    print(separator_line)
