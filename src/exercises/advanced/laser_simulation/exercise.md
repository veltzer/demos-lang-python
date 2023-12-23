Lasers
======

[Credit: this exercise is shamelessly stolen from
http://stackoverflow.com/questions/1480023/code-golf-lasers]

You are given a file such as ``lasers_hit.txt``::

	#########
	#>   \  #
	#  /  x #
	#  \ /  #
	#########

or ``lasers_miss.txt``::

	#########
	#> \ \  #
	#     x #
	#  \ /  #
	#########

which describes a rectangular room.

- The square with ``>`` (could also be ``<`` / ``v`` / ``^``) emits a
	laser beam.

- The laser beam travels empty spaces, and is reflected at 90° by
	``/`` and ``\`` mirrors.

- The ``x`` is the target, ``#`` are walls.

Your goal is to determine whether the beam ends up hitting the target,
or anything else (wall, or in rare cases the emitter). Cute, ha?

For starters, assume the beam emitter is at (1, 1) and points to the
right. When the rest works, look for the emitter.

**Hints**:

- ``open(fname).readlines()`` returns a list of lines.

- At any point, your state can be described by (x, y, direction).

- The next (x, y) is determined by current (x, y) plus the direction.

- The next direction is determined by room[y][x] and current direction.

- Try to use dictionaries instead of long repetitive if..elif
	statements. Think about what you learned in the Map and RPN
	calculator exercises...

- Add debugging prints to display your position after every iteration.

Solution: ``lasers.py``
