def fib():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


class Fib:
    def __init__(self):
        self.a = self.b = 1

    def get(self):
        res = self.a
        self.a, self.b = self.b, self.a + self.b
        return res


f = Fib()
i = 0
while i < 10:
    print(f.get())
    i += 1
i = 0
for x in fib():
    if i >= 10:
        break
    i += 1
    print(x)
