num = int(input('Please enter number of elements: '))
my_list = []
for x in range(num):
    current = int(input('Please enter element' + str(x) + ': '))
    my_list.append(current)
for x in range(0, num - 1, 2):
    [my_list[x], my_list[x + 1]] = [my_list[x + 1], my_list[x]]
print(my_list)
