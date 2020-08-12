"""
This example shows how to use the 'range' iterator.

Notes:
- in python2.7 there was a great different in the performance
of 'range' vs. 'xrange'. 'range' built the entire list in advance
while 'xrange' only iterated the given list.
- in python3 'xrange' is gone. 'range' has the efficiency of python2.7's
'xrange' and so you don't have to worry about any of these.
"""

print('range(10)')
for i in range(10):
    print(i)
print('range(5, 10)')
for i in range(5, 10):
    print(i)
print('range(2, 10, 3)')
for i in range(2, 10, 3):
    print(i)
print('range(11, 2, -3)')
for i in range(11, 2, -3):
    print(i)

# lets write our own range function
def simple_range(stop, start=0, step=1):
    count = start 
    while count < stop:
        yield count
        count +=  step
    raise StopIteration()

print('simple_range(10)')
for i in simple_range(10):
    print(i)
print('simple_range(5, 10)')
for i in simple_range(5, 10):
    print(i)
print('simple_range(2, 10, 3)')
for i in simple_range(2, 10, 3):
    print(i)
