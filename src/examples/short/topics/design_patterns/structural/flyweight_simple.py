"""
An Example of the flyweight pattern in python. The idea is to use the scoping rules of python (instance,
class,module,global) to make the flyweight feel natural. It seems that in python this pattern is much
more natural than in other languages.

Notice that we don't need to write any getters as we just use instance.[attribute] to get the attribute
[attribute]... I wrote one getter just for educational purposes.

Technically speaking we can avoid writing setters too.
"""


class Button:
    text = "no text"
    color = "blue"
    weight = 3

    def __init__(self):
        # look! nothing in init...
        pass

    def printMe(self):
        print(f"text {self.text}")
        print(f"color {self.color}")
        print(f"weight {self.weight}")

    def setText(self, text):
        self.text = text

    def setColor(self, color):
        self.color = color
    
    def setWeight(self, weight):
        self.weight = weight

    def getColor(self):
        if "color" in self.__dict__:
            return self.color
        return Button.color

if __name__ == "__main__":
    b1 = Button()
    assert b1.text == "no text"
    assert b1.color == "blue"
    assert b1.weight == 3
    b1.text = "b1 text"
    b1.color = "red"
    b1.weight = 4
    b1.printMe()
    b2 = Button()
    b2.printMe()
    b2.text = "b2 text"
    b2.printMe()
