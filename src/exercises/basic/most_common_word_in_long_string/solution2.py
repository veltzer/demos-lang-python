from typing import Dict

s = """To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,"""

d: Dict[str, int] = {}
current_max = 0
current_word = None
for word in s.split(" "):
    if word in d:
        d[word] += 1
        if d[word] > current_max:
            current_max = d[word]
            current_word = word
    else:
        d[word] = 1

print(f"{current_word} {current_max}")
