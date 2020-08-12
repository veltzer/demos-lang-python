def right_align_to(lines, width):
    """Right-align all lines to given width."""
    result = []
    for line in lines:
        result.append(line.rjust(width))
    return result


for line in right_align_to(['foo', 'x', '12345678'], 8):
    print(line)
