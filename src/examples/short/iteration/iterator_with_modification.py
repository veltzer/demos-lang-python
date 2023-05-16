"""
The purpose of this example is to show what happens when we modify elements
while iterating. What is the moral of this example? DONT DO IT. Do not modify
data structures while you are iterating them. Mind you that python,unlike
other languages like Java,will not protect you in the least from doing these
types of mistakes. You may get an exception,if you are lucky! So if you
go down this path you are responsible for all your wrong doings...

If you are not lucky no exception will be thrown and you may:
- iterate the same element twice.
- skip certain elements.

What about dictionary?
Well python gives you a little bit more protection here. The iterator will notice
that the size of the dictionary has changed and will generate a RuntimeError exception
when it notices it. See the relevant examples that try to add and remove elements
from a dictionary while iterating it.

What about changing the data structure via the iterator (like in Java) ?
Not supported since the iterators are not intended to be used directly. See the
relevant example.
"""

print("""
example number 1: removing elements in the list in the position before
the place where we are in. Result: Certain elements are never visited.
""")
size = 10
my_list = list(range(size))
elements_visited1 = set()
all_elements1 = set(my_list)
for i, x in enumerate(my_list):
    if i == size // 2:  # integral division
        my_list.pop(0)
        my_list.pop(0)
        my_list.pop(0)
    elements_visited1.add(x)
if len(elements_visited1) != size:
    print(f"elements_visited1 is {len(elements_visited1)} while size is {size}")
    print("This can cause problems for various algorithms")
print(f"elements not visited are {all_elements1 - elements_visited1}")
print("remember that the element removed was 0...")

print("""
example number 2: removing elements in the list in the position before
the place where we are in but doing it on the last element
""")
size = 10
my_list = list(range(size))
elements_visited2 = set()
all_elements2 = set(my_list)
for i, x in enumerate(my_list):
    if i == size - 1:
        my_list.pop(0)
    try:
        # pylint: disable=unnecessary-list-index-lookup
        elements_visited2.add(my_list[i])
    except IndexError:
        print("yes,got errors when accessing l[i]")
if len(elements_visited2) != size:
    print(f"elements_visited2 is {len(elements_visited2)} while size is {size}")
    print("This can cause problems for various algorithms")

print("example number 3: adding elements before the position that we are in")
size = 10
my_list = list(range(size))
elements_visited3 = set()
all_elements3 = set(my_list)
for i, x in enumerate(my_list):
    if i == size // 2:  # integral division
        for y in range(3):
            my_list.insert(0, 10 + y)
    if x in elements_visited3:
        print(f"yep. we are visiting {x} twice...")
    elements_visited3.add(x)
if len(elements_visited3) != len(my_list):
    print(f"elements_visited3 is {len(elements_visited3)} while size is {len(my_list)}")
    print("This can cause problems for various algorithms")

print("example number 4: adding elements to a dictionary while iterating it")
try:
    d = {"one": "ehad", "two": "shnaim", "three": "shalosh"}
    all_elements4 = set(d.keys())  # type: ignore
    elements_visited4 = set()
    i = 0
    for k, v in d.items():
        if i == 1:
            d["four"] = "arba"
        elements_visited4.add(k)
        i += 1
except RuntimeError as e:
    print(f"yes,got runtime error when trying to modify the exception: {e}")

print("example number 5: removing elements to a dictionary while iterating it")
try:
    d = {"one": "ehad", "two": "shnaim", "three": "shalosh"}
    all_elements5 = set(d.keys())
    elements_visited5 = set()
    i = 0
    for k, v in d.items():
        if i == 1:
            del d["one"]
        elements_visited5.add(k)
        i += 1
except RuntimeError as e:
    print(f"yes,got runtime error when trying to modify the exception: {e}")

print("""
example number 6: adding and removing elements in dictionary while iterating it
thus keeping the size of the dictionary the same.
Notice that we do not get an exception in this case.
""")
d = {"one": "ehad", "two": "shnaim", "three": "shalosh"}
all_elements6 = set(d.keys())
elements_visited6 = set()
i = 0
for k, v in d.items():
    if i == 1:
        d["four"] = "arba"
        d["five"] = "hamesh"
        d["six"] = "shesh"
        del d["one"]
        del d["two"]
        del d["three"]
    elements_visited6.add(k)
    i += 1
print(f"elements not visited are {all_elements6 - elements_visited6}")
print(f"elements visited are {elements_visited6}")
print("and you can see we have old and new elements visited")
if len(elements_visited6) != len(all_elements6):
    print(f"elements_visited is {len(elements_visited6)} while size is {len(all_elements6)}")
    print("This can cause problems for various algorithms")
