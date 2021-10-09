"""
Simple implementation of a hangman game.

>>> guess('e')
Yes! 'e' appears 2 times:
?e??e?
>>> guess('x')
Bzzz! No 'x' there.
?e??e?
"""

# Initialization
WORD = 'secret'
open_letters = set()


def print_known_parts():
    """Reveal guessed letters, ? for hidden letters."""
    res = []
    for current in WORD:
        if current in open_letters:
            res.append(current)
        else:
            res.append('?')
    print(''.join(res))


def guess(letter):
    """Call this to play."""
    open_letters.add(letter)
    if letter in WORD:
        print('Yes! \'%s\' appears %s times:' % (letter, WORD.count(letter)))
    else:
        print('Bzzz! No \'%s\' there.' % letter)
    print_known_parts()


# test if run directly, print if imported
if __name__ == '__main__':
    import doctest

    doctest.testmod()
else:
    print_known_parts()
