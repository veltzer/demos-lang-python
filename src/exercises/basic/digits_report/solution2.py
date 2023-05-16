s = input("Please enter a line of digits: ")
my_list = [0] * 10
already_moron = False
for d in s:
    if d.isdigit():
        my_list[int(d)] += 1
    else:
        if not already_moron:
            print("you moron")
            already_moron = True
if not already_moron:
    print(my_list)
