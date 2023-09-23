"""
This example shows how to use the "range" iterator.
"""

print("range(10)")
for i in range(10):
    print(i)
print("range(5, 10)")
for i in range(5, 10):
    print(i)
print("range(2, 10, 3)")
for i in range(2, 10, 3):
    print(i)
print("range(11, 2, -3)")
for i in range(11, 2, -3):
    print(i)


# lets write our own range function
def simple_range(stop, start=0, step=1):
    count = start
    while count < stop:
        yield count
        count += step


print("simple_range(10)")
for i in simple_range(10):
    print(i)
print("simple_range(5, 10)")
for i in simple_range(5, 10):
    print(i)
print("simple_range(2, 10, 3)")
for i in simple_range(2, 10, 3):
    print(i)
