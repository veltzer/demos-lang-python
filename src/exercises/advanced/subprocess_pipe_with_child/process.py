"""
process
"""

import random


for i in range(100000):
    r = random.random()
    print(f"junk {r}")
    if r < 0.001:
        print("secret=12345678")
