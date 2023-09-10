import sys

data = []
# data = list()

# with open("test.txt", "rt") as stream:
#     for line in stream:
#         line = line.rstrip()
#         data.append(line.split(" "))

for line in sys.stdin:
    line = line.rstrip()
    data.append(line.split(" "))

# print(data)
# sys.exit(1)
# max_width = []
# for k in data[1]:
#     max_width.append(0)
max_widths = [0] * len(data[0])
for row in data:
    for i, value in enumerate(row):
        max_widths[i] = max(max_widths[i], len(value))

for row in data:
    for i, value in enumerate(row):
        # print(value+ " " * (max_widths[i] - len(value) + 1), end="")
        print(value+ " " * (max_widths[i] - len(value)+1)+"|", end="")
    print()
