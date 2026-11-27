"""
@author: Gordeev Andrey <gordeev.and.and@gmail.com>

*TL;DR
Provides recombination business logic by chaining together using boolean logic.
"""

from abc import abstractmethod
from typing import Any, override


class Specification:
    def and_specification(self, candidate: Any):
        raise NotImplementedError

    def or_specification(self, candidate: Any):
        raise NotImplementedError

    def not_specification(self):
        raise NotImplementedError

    @abstractmethod
    def is_satisfied_by(self, candidate: object) -> bool:
        raise NotImplementedError


class CompositeSpecification(Specification):
    @abstractmethod
    def is_satisfied_by(self, candidate: object) -> bool:
        raise NotImplementedError

    @override
    def and_specification(self, candidate: Any) -> AndSpecification:
        return AndSpecification(self, candidate)

    @override
    def or_specification(self, candidate: Any) -> OrSpecification:
        return OrSpecification(self, candidate)

    @override
    def not_specification(self) -> NotSpecification:
        return NotSpecification(self)


class AndSpecification(CompositeSpecification):
    def __init__(self, one: Specification, other: Specification) -> None:
        self._one: Specification = one
        self._other: Specification = other

    def is_satisfied_by(self, candidate: object) -> bool:
        return self._one.is_satisfied_by(candidate) and self._other.is_satisfied_by(candidate)


class OrSpecification(CompositeSpecification):
    def __init__(self, one: Specification, other: Specification) -> None:
        self._one: Specification = one
        self._other: Specification = other

    def is_satisfied_by(self, candidate: object) -> bool:
        return self._one.is_satisfied_by(candidate) or self._other.is_satisfied_by(candidate)


class NotSpecification(CompositeSpecification):
    def __init__(self, wrapped: Specification) -> None:
        self._wrapped: Specification = wrapped

    def is_satisfied_by(self, candidate: object) -> bool:
        return not self._wrapped.is_satisfied_by(candidate)


class User:
    def __init__(self, *, super_user: bool = False) -> None:
        self.super_user = super_user


class UserSpecification(CompositeSpecification):
    def is_satisfied_by(self, candidate: object) -> bool:
        return isinstance(candidate, User)


class SuperUserSpecification(CompositeSpecification):
    def is_satisfied_by(self, candidate: object) -> bool:
        return bool(getattr(candidate, "super_user", False))


def main() -> None:
    """
    >>> andrey = User()
    >>> ivan = User(super_user=True)
    >>> vasiliy = "not User instance"

    >>> root_specification = UserSpecification().and_specification(SuperUserSpecification())

    # Is specification satisfied by <name>
    >>> root_specification.is_satisfied_by(andrey), "andrey"
    (False, "andrey")
    >>> root_specification.is_satisfied_by(ivan), "ivan"
    (True, "ivan")
    >>> root_specification.is_satisfied_by(vasiliy), "vasiliy"
    (False, "vasiliy")
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
