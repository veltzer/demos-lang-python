"""
solution to the substring exercise
"""


def substring(string1: str, string2: str) -> bool:
    """ substring implemenetation """
    if len(string2) < len(string1):
        return False
    return any(string2[i:i + len(string1)] == string1 for i in range(len(string2) - len(string1) + 1))


assert substring("hi", "Ship")
assert not substring("shi", "Ship")
assert not substring("Ship", "Shi")
