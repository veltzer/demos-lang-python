class MyDescriptor(object):
    def __set__(self, instance, value):
        print("in set")

    def __get__(self, instance, value):
        print("in get")


class MyClass(object):
    desc = MyDescriptor()
    x = 10
    y = 20


c = MyClass()
c.age = 10
