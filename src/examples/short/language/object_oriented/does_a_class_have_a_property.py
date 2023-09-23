"""
This is an exploration of how to find out if a class has a property.
There are two ways to do it: cls.__dict__ and hasattr.
"""


class A:
    var_foo = "value_foo"
    var_bar = "value_bar"

    @classmethod
    def do_i_have_it(cls, prop):
        return prop in cls.__dict__

    @classmethod
    def do_i_have_it2(cls, prop):
        return hasattr(cls, prop)


print(A.do_i_have_it("var_foo"))
print(A.do_i_have_it("var_bar"))
print(A.do_i_have_it("var_zoo"))
print(A.do_i_have_it2("var_foo"))
print(A.do_i_have_it2("var_bar"))
print(A.do_i_have_it2("var_zoo"))
