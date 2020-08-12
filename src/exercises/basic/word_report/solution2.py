INPUT_NAME = 'tmp.txt'
OUTPUT = 'tmp2.txt'
word_counts = {}
for word in open(INPUT_NAME).read().split():
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
f = open(OUTPUT, 'w')
for word, count in word_counts.items():
    f.write('%s appears %s times\n'.format(word, count))
f.close()
