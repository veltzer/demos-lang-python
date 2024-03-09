from typing import Dict

s = """To be, or not to be, that is the question:
Whether tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,"""

d: Dict[str, int] = {}
for word in s.split(" "):
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

current_max = 0
current_word = None
for k, v in d.items():
    if v > current_max:
        current_max = v
        current_word = k
print(f"{current_word} {current_max}")
