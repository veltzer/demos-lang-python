"""
This solution uses lambda and apply (advanced stuff)
"""


def my_apply(function, seq):
    """ apply a function on a sequence """
    for item in seq:
        function(item)


def reverse_hash(my_dict):
    """ reverse a hash table """
    target = {}
    # pylint: disable=unnecessary-dunder-call
    my_apply(lambda k: target.__setitem__(my_dict[k], k), my_dict)
    # this will create a compilation error
    # my_apply(lambda k: target[d[k]]=k,orig)
    return target


def reverse_hash_map(my_dict):
    """ reverse a hash table using map
    note that map is lazy in python 3, so we must consume the
    resulting iterator (e.g. with list) for the side effects to happen """
    target: dict[str, str] = {}
    # pylint: disable=unnecessary-dunder-call
    list(map(lambda k: target.__setitem__(my_dict[k], k), my_dict))  # noqa: C417
    return target


def main():
    """ the main function """
    orig = {
        "Israel": "Jerusalem",
        "France": "Paris",
        "Italy": "Rome",
        "Egypt": "Cairo",
    }
    print(reverse_hash(orig))
    print(reverse_hash_map(orig))


main()
