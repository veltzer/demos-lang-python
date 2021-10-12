def add1(f):
    def inner(*args, **kw):
        return f(*args, **kw) + 1

    return inner


def makeAList(f):
    def inner(*args, **_kw):
        #    return [f(x) for x in args]
        l = []
        for x in args:
            l.append(f(x))
        return l

    return inner


@makeAList
def square(x):
    return x * x


# pylint: disable=too-many-function-args
print(square(3, 2, 1))
