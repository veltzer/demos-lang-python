def substring(s1, s2):
    return s2.find(s1) != -1


assert substring("hi", "Ship")
assert not substring("shi", "Ship")
assert not substring("Ship", "Shi")
