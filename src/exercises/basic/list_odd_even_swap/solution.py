"""
solution
"""

size = int(input("please enter a list size: "))
number_list = []
for number in range(0, size):
    num = int(input("please enter a number " + str(number) + ": "))
    number_list.append(num)
for number in range(0, size):
    if number / 2 == 0:
        temp = number_list[number]
        number_list[number] = number_list[number + 1]
        number_list[number + 1] = temp
print(number_list)
