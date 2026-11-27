"""
A simple implementation of the visitor pattern
"""


from typing import override


class VisitInterface:
    """
    pure interface to the visit method
    """
    def visit(self):
        raise NotImplementedError


class Node(VisitInterface):
    @override
    def visit(self):
        raise NotImplementedError


class A(Node):
    @override
    def visit(self):
        print("in A")


class B(Node):
    @override
    def visit(self):
        print("in B")


class C(VisitInterface):
    def __init__(self):
        self.a = A()
        self.b = B()

    @override
    def visit(self):
        print("in C")
        self.a.visit()
        self.b.visit()


def main():
    c = C()
    c.visit()


if __name__ == "__main__":
    main()
