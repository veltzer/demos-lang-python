"""
Solution
"""

my_min = 1000000000000000000000
my_max = -1000000000000000000000
for x in range(0, 10):
    num = int(input("give me a number "))
    # pylint: disable=consider-using-min-builtin
    if num < my_min:
        my_min = num
    # pylint: disable=consider-using-max-builtin
    if num > my_max:
        my_max = num
print(my_min, my_max)
