import sys

data = []

for line in sys.stdin:
    line = line.rstrip()
    data.append(line.split(" "))
# max_width = []
# for k in data[1]:
#     max_width.append(0)
max_width = [0] * len(data[1])
for datum in data:
    i = 0
    for datoi in datum:
        max_width[i] = max(max_width[i], len(datoi))
        i += 1
for datum in data:
    i = 0
    for datoi in datum:
        print(datoi + " " * (max_width[i] - len(datoi) + 1), end="")
        i += 1
    print()
