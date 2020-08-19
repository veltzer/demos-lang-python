"""
Simple implementation of a hangman game.

>>> h1=Hangman('banana', mistakes_allowed=2)
??????: 2 mistakes allowed
>>> h2=Hangman('cinnamon')
????????: 5 mistakes allowed
>>> h1.guess('a')
Yes! 'a' appears 3 times:
?a?a?a: 2 mistakes allowed

Sometimes you make mistakes:

>>> h1.guess('h')
Bzzz! No 'h' there.
?a?a?a: 1 mistakes allowed

Game objects are independent:

>>> h2
????????: 5 mistakes allowed
>>> h2.guess('n')
Yes! 'n' appears 3 times:
??nn???n: 5 mistakes allowed
>>> h1
?a?a?a: 1 mistakes allowed

>>> h1.guess('n')
Yes! 'n' appears 2 times:
?anana: 1 mistakes allowed
>>> h1.guess('b')
Yes! 'b' appears 1 times:
banana: YOU WON!

"""


class SimpleHangman:
    """
    Simple hangman game playable from the interpreter.

    No limit on the number of mistakes.
    Doesn't detect victory either.

    Call .guess() to play:

    >>> h=SimpleHangman('secret')
    ??????
    >>> h.guess('e')
    Yes! 'e' appears 2 times:
    ?e??e?
    >>> h.guess('x')
    Bzzz! No 'x' there.
    ?e??e?
    """

    def __init__(self, word):
        # Private don't look here!
        self._word = word
        # Public
        self.open_letters = set()
        print(self)

    def known_parts(self):
        """Reveal guessed letters, ? for hidden letters."""
        res = []
        for c in self._word:
            if c in self.open_letters:
                res.append(c)
            else:
                res.append('?')
        return ''.join(res)

    # __repr__ defines how the object is displayed.
    # It's called by 'print' and by the interpreter.
    def __repr__(self):
        """Describe current game state."""
        return self.known_parts()

    def guess(self, letter):
        """Call this to play."""
        self.open_letters.add(letter)
        if letter in self._word:
            print('Yes! \'%s\' appears %s times:' %
                  (letter, self._word.count(letter)))
            print(self)
        else:
            print('No \'%s\' there.' % letter)
            print(self)


class Hangman(SimpleHangman):
    """
    Hangman game playable from the interpreter.

    Counts mistakes, detects victory and defeat.

    Call .guess() to play:

    >>> h=Hangman('secret', 1)
    ??????: 1 mistakes allowed
    >>> h.guess('e')
    Yes! 'e' appears 2 times:
    ?e??e?: 1 mistakes allowed
    >>> h.guess('x')
    Bzzz! No 'x' there.
    ?e??e?: 0 mistakes allowed
    >>> h.guess('x')
    You already tried 'x'.
    ?e??e?: 0 mistakes allowed
    >>> h.guess('z')
    Bzzz! No 'z' there.
    ?e??e?: GAME OVER
    """

    def __init__(self, word, mistakes_allowed=5):
        self.mistakes_allowed = mistakes_allowed
        # SimpleHangman.__init__ prints self, so self.mistakes_allowed
        # must be defined before we call it.
        SimpleHangman.__init__(self, word)

    def __repr__(self):
        """Describe current game state."""
        if set(self._word) <= self.open_letters:
            return '%s: YOU WON!' % self._word
        if self.mistakes_allowed < 0:
            return '%s: GAME OVER' % self.known_parts()
        return ('%s: %s mistakes allowed' %
                (self.known_parts(), self.mistakes_allowed))

    def guess(self, letter):
        """Call this to play."""
        # bells and whistles
        if set(self._word) <= self.open_letters:
            print('You won. Why do you keep guessing?')
            return
        if self.mistakes_allowed < 0:
            print('You lost. Stop trying.')
            return
        if letter in self.open_letters:
            print('You already tried %s.' % letter)
            print(self)
            return

        if letter not in self._word:
            self.mistakes_allowed -= 1
        SimpleHangman.guess(self, letter)


# test if run directly, do nothing if imported
if __name__ == '__main__':
    import doctest

    doctest.testmod()
