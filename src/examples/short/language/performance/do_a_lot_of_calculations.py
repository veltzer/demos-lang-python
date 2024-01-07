"""
This is an example exploring how much does namespace lookup cost.

Solution: cache your globals
"""

i = 0
my_sum = 0
while True:
    my_sum += i * i
    i += 1
