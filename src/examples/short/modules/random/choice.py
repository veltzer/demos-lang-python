"""
This is a demo of the random.choice function

References:
- https://docs.python.org/3/library/random.html
"""

from random import choice, choices

people: list[str] = ["Bob", "Tom", "James", "Sandra"]
print(choice(people))

weights: tuple = (.15, .20, .35, .30)
print(f"choices()={choices(people, k=5, weights=weights)}")
