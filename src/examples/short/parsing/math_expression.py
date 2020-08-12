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

    def number(self, tup, buf):
        print('in number')
        '''Process the given production and it's children'''

    def expr(self, tup, buf):
        print('in expr')
        '''Process the given production and it's children'''

    def __call__(self, value, data):
        print('value is ' + str(value))
        print('data is ' + str(data))
        return value
        # return super(self.__class__,self).__call__(self,value,data)


class MyParser(simpleparse.parser.Parser):
    def buildProcessor(self):
        return MyProcessorClass()


parser = MyParser(declaration, 'full')
pprint.pprint(parser.parse(sys.argv[1]))
