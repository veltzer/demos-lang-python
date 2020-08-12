"""
This is an exploration of how to find out if a class has a property.
There are two ways to do it: cls.__dict__ and hasattr.
"""


class A:
    foo = 'foo'
    bar = 'bar'

    @classmethod
    def do_i_have_it(cls, prop):
        return prop in cls.__dict__

    @classmethod
    def do_i_have_it2(cls, prop):
        return hasattr(cls, prop)


print(A.do_i_have_it('foo'))
print(A.do_i_have_it('bar'))
print(A.do_i_have_it('zoo'))
print(A.do_i_have_it2('foo'))
print(A.do_i_have_it2('bar'))
print(A.do_i_have_it2('zoo'))
