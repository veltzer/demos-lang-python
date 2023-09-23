"""
This is an exploration of how one class method calls another.
"""


class A:
    @classmethod
    def method_bar(cls, p):
        print("method_bar", p)

    @classmethod
    def method_foo(cls, p):
        print("method_foo", p)
        cls.method_bar("param for method_bar")


A.method_foo("param for method_foo")
