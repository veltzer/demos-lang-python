#! /usr/bin/python

def frange(start, stop, step=0.25):
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
