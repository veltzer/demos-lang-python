import sys
import operator


def get_second_item(t):
    return t[1]


if len(sys.argv) != 2:
    print("Please specify input file name", file=sys.stderr)
    sys.exit(1)
filename = sys.argv[1]
words = {}
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        for word in line.split(" "):
            if word not in words:
                words[word] = 0
            words[word] += 1
my_list = list(words.items())
# my_list.sort(key=get_second_item, reverse=True)
my_list.sort(key=operator.itemgetter(1), reverse=True)
print(my_list[:3])
# print("\n".join(map(operator.itemgetter(0), my_list[:3])))
