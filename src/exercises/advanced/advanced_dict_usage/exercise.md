# Advanced Dist Usage

You're given a dictionary representing a (very simplified) map of
Frodo's travels around Middle Earth::

```python
places = {
'Shire': {'leave': 'Bree', 'stay': 'DEATH'},
'DEATH': {},
'Bree': {'with Strider': 'Rivendell', 'alone': 'DEATH'},
'Rivendell': {'over mountains': 'DEATH', 'through Moria': 'Lorien'},
'Lorien': {'down Anduin': 'Falls of Rauros'},
'Falls of Rauros': {'down Anduin': 'Minas Tirith', 'east': 'Ithilien'},
'Ithilien': {'south': 'Black Gate'},
'Black Gate': {'in': 'DEATH', 'follow Gollum': 'Minas Morgul'},
'Minas Morgul': {'road': 'DEATH', 'tunnel': 'Mordor'},
'Mordor': {'eagles': 'Minas Tirith'},
'Minas Tirith': {'return home': 'Shire (tired)'},
'Shire (tired)': {'stay': 'Shire (tired)', 'retire': 'the West'},
'the West': {}
}
```

For each place there is a sub-dictionary mapping actions Frodo could
take and where they would lead him. (Many lead to 'DEATH', from which
there are no more actions possible ;-).

## Walk

Such a dictionary is all you need for a (very simple) text-based
role-playing game! Each time it should print the current place and
the list of actions, and ask the user which action to take.

Bonuses: present a nice interface, don't crush on illegal input, allow
exiting the game.

## Hints(1)
* `input()` reads a line from the user and returns it.

Solution: `solution1.py`

## Search

You're now in Rivendell, and you've just volunteered to take the ring
to Mordor, though you do not know the way. Can you write a program
that tries to find a way?

For simplicity, we're only looking for sequences of at most 7 actions.

If it simplifies matters for you, you don't have to find the sequence
of actions, just check *whether* its possible (in no more than 7
steps).

## Hints(2)

* If you have no idea how to solve this, here is a simple approach
that works. You'll maintain a dictionary of places to which you
know the way (the keys will be the action sequences to reach them).

* Initialize it with only 'Rivendell' (the way to which is [] - no actions required).

* Repeat 7 times: for any place P to which you know the way, for any action A leading from P to Q to which you don't yet know the way, set `way_to[Q] = way_to[P] + [A]`.

* If you get a "dictionary changed size during iteration" error, it means you should do `for k in dictionary.keys():` instead of `for k in dictionary:`.

Still lost? Read the solution, its shorter that you'd expect.

Solution: `solution2.py`
