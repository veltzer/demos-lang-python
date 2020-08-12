"""
This example shows how to find whether a string contains a digit fast.

References:
- https://stackoverflow.com/questions/17681655/python-if-a-word-contains-a-digit
"""


def has_digits(word: str) -> bool:
    return any(ch.isdigit() for ch in word)


print(has_digits("b747"))
print(has_digits("alpha"))
