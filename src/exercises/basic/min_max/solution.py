my_min = 1000000000000000000000
my_max = -1000000000000000000000
for x in range(0, 10):
    num = int(input("give me a number "))
    if num < my_min:
        my_min = num
    if num > my_max:
        my_max = num
print(my_min, my_max)
