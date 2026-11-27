""" solution """

import sys

data = []
# data = list()  # noqa: ERA001  teaching: kept in the comment for the reader

# with open("test.txt", "rt") as stream:
#     for line in stream:
#         line = line.rstrip()  # noqa: ERA001  teaching: kept in the comment for the reader
#         data.append(line.split(" "))  # noqa: ERA001  teaching: kept in the comment for the reader

for raw_line in sys.stdin:
    line = raw_line.rstrip()
    data.append(line.split(" "))

# print(data)  # noqa: ERA001  teaching: kept in the comment for the reader
# sys.exit(1)  # noqa: ERA001  teaching: kept in the comment for the reader
# max_width = []  # noqa: ERA001  teaching: kept in the comment for the reader
# for k in data[1]:
#     max_width.append(0)  # noqa: ERA001  teaching: kept in the comment for the reader
max_widths = [0] * len(data[0])
for row in data:
    for i, value in enumerate(row):
        max_widths[i] = max(max_widths[i], len(value))

for row in data:
    for i, value in enumerate(row):
        # print(value + " " * (max_widths[i] - len(value) + 1), end="")  # noqa: ERA001  teaching: kept in the comment for the reader
        print(value + " " * (max_widths[i] - len(value) + 1) + "|", end="")
    print()
