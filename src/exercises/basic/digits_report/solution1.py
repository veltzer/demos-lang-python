# this is a solution to the digits counting exercise...

s = input("Please enter a line of digits: ")
# lets initialize a 10 element list where all elements are 0
my_list = [0] * 10
# iterate all digits in the input...
for d in s:
    if ord("0") <= ord(d) <= ord("9"):
        my_list[int(d)] += 1
    else:
        print("you gave me bad data, error")
        break
else:
    # output a "simple" report (just showing the counters...)
    # print(my_list)
    for n, counter in enumerate(my_list):
        print(f"{n} appeared {counter} times in the text")
