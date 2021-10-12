INPUT_NAME = 'tmp.txt'
OUTPUT = 'tmp2.txt'
word_counts = {}
with open(INPUT_NAME) as f:
    for word in f.read().split():
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
with open(OUTPUT, 'w') as f:
    for word, count in word_counts.items():
        f.write(f"{word} appears {count} times\n")
