""" not_fair_2.py """


def substring(s1: str, s2: str):
    return s2.find(s1) != -1


assert substring("hi", "Ship")
assert not substring("shi", "Ship")
assert not substring("Ship", "Shi")
