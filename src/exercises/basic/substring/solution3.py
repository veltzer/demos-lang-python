"""
solution to the substring exercise
"""


def substring(string1, string2):
    """ substring implemenetation """
    if len(string2) < len(string1):
        return False
    for i in range(len(string2) - len(string1) + 1):
        if string2[i:i + len(string1)] == string1:
            return True
    return False


assert substring("hi", "Ship")
assert not substring("shi", "Ship")
assert not substring("Ship", "Shi")
