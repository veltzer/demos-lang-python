s = input('Please enter a line of digits: ')
l = [0] * 10
already_moron = False
for d in s:
    if d.isdigit():
        l[int(d)] += 1
    else:
        if not already_moron:
            print('you moron')
            already_moron = True
if not already_moron:
    print(l)
