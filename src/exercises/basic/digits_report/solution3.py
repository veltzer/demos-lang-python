s = input('Please enter a line of digits: ')
l = [0] * 10
for d in s:
    if '0' <= d <= '9':
        l[int(d)] += 1
print(l)
