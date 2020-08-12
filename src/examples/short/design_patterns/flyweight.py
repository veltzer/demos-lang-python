"""
An Example of the flyweight pattern in python. The idea is to use the scoping rules of python (instance,
class,module,global) to make the flyweight feel natural. It seems that in python this pattern is much
more natural than in other languages.
"""


class Button:
    color = 'blue'
    text = 'no text'
    weight = 3
    bgColor = 7

    def __init__(self):
        # look Ma! nothing in init...
        pass

    def printMe(self):
        print('color', self.color)
        print('text', self.text)

    def setText(self, text):
        self.text = text

    def setColor(self, color):
        self.color = color

    def getColor(self):
        if 'color' in self.__dict__:
            return self.color
        else:
            return Button.color

    def getWeight(self):
        return self.weight


b1 = Button()
b2 = Button()
b1.printMe()
b2.printMe()
b1.setColor('green')
b1.printMe()
b2.printMe()

Button.color = 'red'
b1.printMe()
b2.printMe()
# print(b1.color)
# print(b1.weight)
# print(dir(b1))


'''
b2=Button()
print(Button.color)
print(b1.getColor())
print(b1.weight)
print(b1.getWeight())
b1.setColor('white')
b2.setColor('black')
b1.doSomething()
b2.doSomething()
Button.text='new text'
b1.doSomething()
b2.doSomething()
print(b1.__dict__)
print(b2.__dict__)
#print(dir(b))
'''
