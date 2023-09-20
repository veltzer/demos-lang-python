

# this is the "regular" or "non-functional"
# version of the code
# this style of programming is called "imperative programming"
l1 = []
for x in range(2,8):
    l1.append(x * x)
print(l1)

# now we will write a "functional" style version of the above code
l2 = list(map(lambda x: x * x, range(2,8)))
print(l2)

# THE SECOND VERSION IS MUCH MUCH MUCH BETTER FOR OPTIMIZATION!
