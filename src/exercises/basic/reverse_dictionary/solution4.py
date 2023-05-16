"""
lambda and apply again...
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


def main():
    """ the main function """
    orig = {
        "Israel": "Jerusalem",
        "France": "Paris",
        "Italy": "Rome",
        "Egypt": "Cairo",
    }
    print(reverse_hash(orig))


main()
