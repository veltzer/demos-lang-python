"""
Solution
"""

my_min = 1000000000000000000000
my_max = -1000000000000000000000
for _x in range(10):
    num = int(input("give me a number "))
    my_min = min(my_min, num)
    my_max = max(my_max, num)
print(my_min, my_max)
