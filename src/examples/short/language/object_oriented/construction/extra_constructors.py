"""
Example of how to create more than one constructor for a class.

Notes:
- You should not create an object of type "A" in the "from_q"
method below but rather an object type of "cls" since the method
might be called on a subclass and in that case the class created
for the user should be the subclass and not the parent class.
- the "classmethod" decoration serves two purposes. One is to make
sure that we get passed the "cls" parameter which is very important
(see above). The second is to make sure that this method will be
called on the class and not on an instance.
"""


class A:
    def __init__(self, p):
        self.p = p

    def __str__(self):
        return str(self.p)

    @classmethod
    def from_q(cls, q):
        return cls(-q)

    @staticmethod
    def static_from_q(q):
        return A(-q)


class B(A):
    pass


o1 = A(1)
print(o1)
print(type(o1))

o2 = A.from_q(-2)
print(o2)
print(type(o2))

o3 = B(3)
print(o3)
print(type(o3))

o4 = B.from_q(-4)
print(o4)
print(type(o4))
