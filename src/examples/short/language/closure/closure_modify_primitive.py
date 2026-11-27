"""
This is an example that shows that you cannot change primitives in closures.
"""


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def make_adder() -> Callable[[], None]:
    # noinspection PyUnusedLocal
    x = 0

    def adder() -> None:
        # noinspection PyUnboundLocalVariable,PyUnresolvedReferences
        x += 1  # noqa: F823  teaching: shows a local name used before its assignment  # pyrefly: ignore[unbound-name]  teaching: x += 1 makes x local, so it is read before assignment
        # noinspection PyUnresolvedReferences
        print(x)

    return adder


f = make_adder()
f()
f()
f()
