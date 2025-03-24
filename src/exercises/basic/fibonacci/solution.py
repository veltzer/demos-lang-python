"""
Solution
"""

x = y = 1
my_counter = 0
my_sum = 0
while my_counter < 100:
    my_sum += x + y
    x, y = y, x + y
    my_counter += 1
print(my_sum)
