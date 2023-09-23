"""
This is an example of a weird pattern in OO python
in which the local attributes of an
instance get populated from the global (class based)
ones.

This is based on the loop
"""


class MyClass:
    var_member = 14

    def __init__(self, member):
        if member:
            self.var_member = member
        else:
            self.var_member = self.var_member

    def do_print(self):
        print(f"var_member is {self.var_member}")


# Lets show how we use our object
b = MyClass(15)
b.do_print()
b = MyClass(16)
b.do_print()
b = MyClass(None)
b.do_print()
