from sortedcontainers import SortedDict

d = SortedDict()
d["b"] = "c"
d["c"] = "c"
d["y"] = "c"
d["a"] = "c"
for k in d.keys():
    print(k)
