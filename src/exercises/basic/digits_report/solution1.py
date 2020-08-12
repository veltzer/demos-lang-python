# this is a solution to the digits counting exercise...

s = input('Please enter a line of digits: ')
# lets initialize a 10 element list where all elements are 0
l = [0] * 10
# iterate all digits in the input...
for d in s:
    if ord('0') <= ord(d) <= ord('9'):
        l[int(d)] += 1
    else:
        print('you gave me bad data, error')
        break
else:
    # output a 'simple' report (just showing the counters...)
    # print(l)
    for n, counter in enumerate(l):
        print(
            '{n} appeared {counter} times in the text'.format(n=n, counter=counter))
