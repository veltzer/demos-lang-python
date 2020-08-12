mymin = 1000000000000000000000
mymax = -1000000000000000000000
for x in range(0, 10):
    num = int(input('give me a number '))
    if num < mymin:
        mymin = num
    if num > mymax:
        mymax = num
print(mymin, mymax)
