class MyDescriptor:
    def __set__(self, instance, value):
        print("in set")

    def __get__(self, instance, value):
        print("in get")


class MyClass:
    desc = MyDescriptor()
    x = 10
    y = 20


c = MyClass()
# pylint: disable=attribute-defined-outside-init
c.age = 10  # type: ignore
