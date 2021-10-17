"""
doing simple arithmetic evaluation in python
"""

import sys

import pyparsing

number = pyparsing.Word(pyparsing.nums).setParseAction(lambda t: int(t[0]))


def number_act(_string, _location, tok):
    return int(tok[0])


number.setParseAction(number_act)

expr = pyparsing.Forward()
operand = number | expr

op_multiply = pyparsing.oneOf('* /')
op_plus = pyparsing.oneOf('+ -')
expr = pyparsing.operatorPrecedence(operand, [
    (op_multiply, 2, pyparsing.opAssoc.LEFT),
    (op_plus, 2, pyparsing.opAssoc.LEFT),
])


def expr_act(s, loc, tok):
    print('in here', s, loc, tok)
    if tok[0][1] == '*':
        return tok[0][0] * tok[0][2]
    if tok[0][1] == '/':
        return tok[0][0] // tok[0][2]
    if tok[0][1] == '+':
        return tok[0][0] + tok[0][2]
    if tok[0][1] == '-':
        return tok[0][0] - tok[0][2]
    return None


expr.setParseAction(expr_act)

expr.setDebug()

print(expr.parseString(sys.argv[1])[0])
