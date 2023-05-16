num = int(input("Please enter number of elements: "))
my_list = list(range(num))
for x in range(num):
    current = int(input("Please enter element" + str(x) + ": "))
    if x % 2 == 0:
        if x == num - 1:
            my_list[x] = current
        else:
            my_list[x + 1] = current
    else:
        my_list[x - 1] = current
print(my_list)
