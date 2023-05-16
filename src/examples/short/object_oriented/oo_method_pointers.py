"""
This example shows how to store method pointers and call them
"""


class MyObj:
    def __init__(self):
        self.curFunc = self.handle_hello
        self.a = 5

    def handle_hello(self, line):
        print("hello got line", line, self.a)

    def doTheCall(self, line):
        print("got line", line)
        self.curFunc(line)


o = MyObj()
o.doTheCall("foobar")
