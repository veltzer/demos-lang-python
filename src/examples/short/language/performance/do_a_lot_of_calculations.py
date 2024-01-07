"""
This is an example exploring how much does namespace lookup cost.

Solution: cache your globals
"""

i=0
sum = 0 
while True:
    sum += i*i
    i += 1
