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
_word = 'secret'
open_letters = set()


def print_known_parts():
    """Reveal guessed letters, ? for hidden letters."""
    res = []
    for c in _word:
        if c in open_letters:
            res.append(c)
        else:
            res.append('?')
    print(''.join(res))


def guess(letter):
    """Call this to play."""
    open_letters.add(letter)
    if letter in _word:
        print('Yes! \'%s\' appears %s times:' % (letter, _word.count(letter)))
    else:
        print('Bzzz! No \'%s\' there.' % letter)
    print_known_parts()


# test if run directly, print if imported
if __name__ == '__main__':
    import doctest

    doctest.testmod()
else:
    print_known_parts()
