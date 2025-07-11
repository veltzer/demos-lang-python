"""
*What is this pattern about?
Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.

*TL;DR
Enables selecting an algorithm at runtime.
"""


from collections.abc import Callable


class DiscountStrategyValidator:  # Descriptor class for check perform
    @staticmethod
    def validate(obj: "Order", value: Callable) -> bool:
        try:
            if obj.price - value(obj) < 0:
                raise ValueError(
                    f"Discount cannot be applied due to negative price resulting. {value.__name__}"
                )
        except ValueError as ex:
            print(str(ex))
            return False
        return True

    def __set_name__(self, owner, name: str) -> None:
        # pylint: disable=attribute-defined-outside-init
        self.private_name = f"_{name}"

    def __set__(self, obj: "Order", value: Callable | None = None) -> None:
        if value and self.validate(obj, value):
            setattr(obj, self.private_name, value)
        else:
            setattr(obj, self.private_name, None)

    def __get__(self, obj: object, objtype: type | None = None):
        return getattr(obj, self.private_name)


class Order:
    discount_strategy = DiscountStrategyValidator()

    def __init__(self, price: float, discount_strategy: Callable | None = None) -> None:
        self.price: float = price
        self.discount_strategy = discount_strategy

    def apply_discount(self) -> float:
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self) -> str:
        strat = getattr(self.discount_strategy,"__name__",None)
        return f"<Order price: {self.price} with discount strategy: {strat}>"


def ten_percent_discount(order: Order) -> float:
    return order.price * 0.10


def on_sale_discount(order: Order) -> float:
    return order.price * 0.25 + 20


def main():
    """
    >>> order = Order(100, discount_strategy=ten_percent_discount)
    >>> print(order)
    <Order price: 100 with discount strategy: ten_percent_discount>
    >>> print(order.apply_discount())
    90.0
    >>> order = Order(100, discount_strategy=on_sale_discount)
    >>> print(order)
    <Order price: 100 with discount strategy: on_sale_discount>
    >>> print(order.apply_discount())
    55.0
    >>> order = Order(10, discount_strategy=on_sale_discount)
    Discount cannot be applied due to negative price resulting. on_sale_discount
    >>> print(order)
    <Order price: 10 with discount strategy: None>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
