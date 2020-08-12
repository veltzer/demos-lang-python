"""
This is an exploration of how one class method calls another.
"""


class A:
    @classmethod
    def bar(cls, p):
        print('bar', p)

    @classmethod
    def foo(cls, p):
        print('foo', p)
        cls.bar('param for bar')


A.foo('param for foo')
