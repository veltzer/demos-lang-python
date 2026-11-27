"""
An Example of the flyweight pattern in python. The idea is to use the scoping rules of python (instance,
class,module,global) to make the flyweight feel natural. It seems that in python this pattern is much
more natural than in other languages.

Notice that we dont need to write any getters as we just use instance.[attribute] to get the attribute
[attribute]... I wrote one getter just for educational purposes.

Technically speaking we can avoid writing setters too.
"""


class Button:
    text = "no text"
    color = "blue"
    weight = 3

    def __init__(self) -> None:
        # look! nothing in init...
        pass

    def print_me(self) -> None:
        print(f"text {self.text}")
        print(f"color {self.color}")
        print(f"weight {self.weight}")

    def set_text(self, text: str) -> None:
        self.text = text

    def set_color(self, color: str) -> None:
        self.color = color

    def set_weight(self, weight: int) -> None:
        self.weight = weight

    def get_color(self) -> str:
        return self.color
        # if "color" in self.__dict__:
        #     return self.color  # noqa: ERA001  teaching: kept in the comment for the reader
        # return Button.color  # noqa: ERA001  teaching: kept in the comment for the reader


if __name__ == "__main__":
    b1 = Button()
    print(b1.__dict__)
    print(b1.color)
    assert b1.text == "no text"
    assert b1.color == "blue"
    assert b1.weight == 3
    b1.text = "b1 text"
    b1.color = "red"
    b1.weight = 4
    b1.print_me()
    b2 = Button()
    b2.print_me()
    b2.text = "b2 text"
    b2.print_me()
