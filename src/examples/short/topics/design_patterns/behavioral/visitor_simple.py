"""
"""


class VisitInterface:
    """
    pure interface to the visit method
    """
    def visit():
        raise NotImplemented()


class Node(VisitInterface):
    pass

class A(Node):
    def visit(self):
        print("in A")


class B(Node):
    def visit(self):
        print("in B")


class C(VisitInterface):
    def __init__(self):
        self.a = A()
        self.b = B()
    def visit(self):
        print("in C")
        self.a.visit()
        self.b.visit()

def main():
    c = C()
    c.visit()


if __name__ == "__main__":
    main()
