



def op(o, x=None, items=[], s=set()):       # the [] is created once, at def time
    if o=="push":
        items.append(x)
        return None
    if o=="pop":
        return items.pop()

op("push",2)
op("push",3)
op("push",4)
print(op("pop"))
print(op("pop"))
op("push",5)
