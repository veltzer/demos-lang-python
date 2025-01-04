#! /usr/bin/python
# Implement single parameter

def frange(start, stop=None, step=0.25):
    if stop is None:
        stop = start
        curr = 0.0
    else: 
        curr = float(start)

    while curr < stop:
        yield curr
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

