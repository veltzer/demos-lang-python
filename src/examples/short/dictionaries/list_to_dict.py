"""
This is an example of how to turn dicts into lists
When we turn a dict into a list we get a list of tuples!!!
Each tuple is a key, value tuple.
Why would you want to do that?
- because you want to copy the data to a list container.
- because you want to sort the data and list.sort needs a list.
- any other reason you can think of.
"""

d = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

# here list receives an iterator as argument
l1=list(d.items())
print(l1)
print(type(l1))

# in this example we construct a list by appending each item
l2=[]
for k, v in d.items():
    l2.append((k, v))
print(l2)
print(type(l2))

# this is WRONG!!!! since d.items() DOES NOT return a list but rather the next element
# every time and should be called from an interator context (e.g. for loop)
l3=d.items()
print(l3)
print(type(l3))
