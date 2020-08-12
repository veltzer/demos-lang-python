s = input('Please enter a line of digits: ')
l = [0] * 10
for d in s:
    l[int(d)] += 1
print(l)
