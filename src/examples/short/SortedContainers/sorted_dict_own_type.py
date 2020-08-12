class Range:
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to
    def __lt__(self, t):
        if type(t) == int:
            return self.to <= t
        return self.to <= t.fr
    def __eq__(self, t):
        if type(t) == int:
            return self.fr <= t and t < self.to
        return self.fr == t.fr and self.to == t.to
    def __ne__(self, t):
        return not self.__eq__(t)
    def __hash__(self):
        return hash(str(self))
    def __str__(self):
        return "[{}-{}]".format(self.fr, self.to)

from sortedcontainers import SortedDict

d = SortedDict()
d[Range(50,60)] = None
d[Range(40,50)] = None
d[Range(10,20)] = None
d[Range(80,90)] = None
d[Range(110,120)] = None
for k in d.keys():
    print(k)
print("==============================")
print("85", d.iloc[d.index(85)])
print("40", d.iloc[d.index(40)])
print("49", d.iloc[d.index(49)])
print("50", d.iloc[d.index(50)])
print("59", d.iloc[d.index(59)])
try:
    d.index(60)
except ValueError:
    print("60 is not in d")
d[60]
