""" solution """

from functools import reduce


# imperative coding
mysum = 0
for x in range(100):
    mysum = mysum + x * x
print(f"mysum is {mysum}")

# functional , declarative coding
m = map(lambda x: x * x, range(100))
result = reduce(lambda a,b: a + b, m)
print(f"result is {result}")
