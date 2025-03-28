""" not_fair.py """


def substring(s1, s2):
    return s1 in s2


assert substring("hi", "Ship")
assert not substring("shi", "Ship")
assert not substring("Ship", "Shi")
