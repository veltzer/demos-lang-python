import pprint
import sys

import simpleparse.dispatchprocessor

declaration = r'''# note use of raw string when embedding in python code...
full        := ws,expr,ws
number        := [0-9eE+.-]+
expr        := number,'+',number/number,'-',number
ws        := [ \t\v]*
'''


class MyProcessorClass(simpleparse.dispatchprocessor.DispatchProcessor):
    # def __init__(self):
    #     print('cons')

    def number(self, _tup, _buf):
        """ Process the given production and it's children """
        print('in number')

    def expr(self, _tup, _buf):
        """ Process the given production and it's children """
        print('in expr')

    def __call__(self, value, data):
        # return super(self.__class__,self).__call__(self,value,data)
        print(f"value is {value}")
        print(f"data is {data}")
        return value


class MyParser(simpleparse.parser.Parser):
    def buildProcessor(self):
        return MyProcessorClass()


parser = MyParser(declaration, "full")
pprint.pprint(parser.parse(sys.argv[1]))
