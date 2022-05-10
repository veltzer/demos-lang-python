import textwrap


def lines2paragraphs(lines):
    """Group lines into paragraphs as lists of lines."""
    paragraph = []
    for line in lines:
        line = line.strip()
        if line == '':
            yield paragraph
            paragraph = []
        else:
            paragraph.append(line)
    # The last paragraph remains
    # (if the input didn't end with an empty line)
    if len(paragraph) > 0:
        yield paragraph


def reformat(lines, chars):
    """
    Bonus: streaming lines->lines reformatter
    Generate lines of reformatted paragraphs.
    Paragraph in input and output are separated by empty lines.
    """
    for para in lines:
        for line in textwrap.wrap(' '.join(para), chars):
            yield line
        yield ''


with open("/usr/share/doc/python/copyright") as f:
    mygen = reformat(lines2paragraphs(f), 50)
    for element in mygen:
        print(element)
