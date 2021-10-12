s = input('Please enter a line of digits: ')
my_list = [0] * 10
for d in s:
    my_list[int(d)] += 1
print(my_list)
