"""
Solution2
"""

mysum = 0
row = 1
while row <= 10:
    col = 1
    while col <= 10:
        mysum += row * col
        col += 1
    row += 1
print(mysum)
