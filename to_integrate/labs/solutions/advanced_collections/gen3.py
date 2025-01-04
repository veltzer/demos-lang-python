#! /usr/bin/python
# Implement single parameter

import decimal


def frange(start, stop=None, step=0.25):
    step = decimal.Decimal(str(step))

    if stop is None:
        stop = decimal.Decimal(str(start))
        curr = decimal.Decimal(0)
    else:
        stop = decimal.Decimal(str(stop))
        curr = decimal.Decimal(str(start))

    if step != 0:
        while curr < stop:
            yield float(curr)
            curr += step


print(list(frange(1, 3)))
print(list(frange(1, 3, 0.33)))
print(list(frange(1, 3, 1)))         # Should return [1.0, 2.0], not [1, 2]
print(list(frange(3, 1)))            # Should return an empty list
print(list(frange(-1, -0.5, 0.1)))

for num in frange(3.142, 12):
    print(f"{num:05.2f}")

print(frange(1,2))

one = list(frange(0, 3.5, 0.25))
two = list(frange(3.5))
if one == two:
    print("Defaults worked!")
else:
    print("Oops!  Defaults did not work")
    print("one:", one)
    print("two:", two)

