"""
Solution3
"""

s = input("Please enter a line of digits: ")
my_list = [0] * 10
for d in s:
    if "0" <= d <= "9":
        my_list[int(d)] += 1
print(my_list)
