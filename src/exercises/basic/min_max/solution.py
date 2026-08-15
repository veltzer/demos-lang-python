"""
Solution
"""

my_min = 1000000000000000000000
my_max = -1000000000000000000000
for x in range(10):
    num = int(input("give me a number "))
    # pylint: disable=consider-using-min-builtin
    my_min = min(my_min, num)
    # pylint: disable=consider-using-max-builtin
    my_max = max(my_max, num)
print(my_min, my_max)
