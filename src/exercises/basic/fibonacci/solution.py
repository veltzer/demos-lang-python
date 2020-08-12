x = y = 1
mycounter = 0
mysum = 0
while mycounter < 100:
    mysum += x + y
    x, y = y, x + y
    mycounter += 1
print(mysum)
