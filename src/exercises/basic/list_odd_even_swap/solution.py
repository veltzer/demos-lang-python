"""
solution
"""

size = int(input('please enter a list size: '))
l = []
for number in range(0, size):
    num = int(input('please enter a number ' + str(number) + ': '))
    l.append(num)
for number in range(0, size):
    if number / 2 == 0:
        temp = l[number]
        l[number] = l[number + 1]
        l[number + 1] = temp
print(l)
