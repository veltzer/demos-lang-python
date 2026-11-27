""" Book.py """


class Book:
    def __init__(self, price: float) -> None:
        """ constructor """
        # call parent constructor
        super().__init__()
        self.__price = price

    def get_price(self):
        """ getter """
        return self.__price

    def set_price(self, new_price: float) -> None:
        """ setter """
        self.__price = new_price

    def print_me(self) -> None:
        """ printing function """
        print("price is", self.__price)
