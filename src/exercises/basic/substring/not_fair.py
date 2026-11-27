""" not_fair.py """


def substring(s1: str, s2: str) -> bool:
    return s1 in s2


assert substring("hi", "Ship")
assert not substring("shi", "Ship")
assert not substring("Ship", "Shi")
