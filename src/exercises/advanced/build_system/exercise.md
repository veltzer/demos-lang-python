Make clone
==========

Make is a tool that reads a file describing files that can be produced
from other files (e.g. executable from sources), and what commands
have to be run to do it (e.g. compiler). It compares file
modification dates, and only regenerates the files whose dependecies
changed.

In this exercise, you'll write a very simplified version of Make.
You'll only handle dependecy lists (without commands) and you'll
ignore file modification times (always assuming everything need to be
rebuilt).

Exercise 5A: parsing
--------------------

Write a function that can parse a file like ``make.txt``::

	all:app
	app:a.o b.o
	a.o:a.c
	b.o:b.c

and return a dictionary giving for each target a list of files on
which it depends::

	{'all': ['app'],
	'a.o': ['a.c'],
	'b.o': ['b.c'],
	'app': ['a.o', 'b.o']}

**Hints**:

- The simplest way to read a file line-by-line is ``for line in
	open("make.txt"):``.

- ``"foo:bar".split(":")`` returns ['foo', 'bar'].

**Bonus**: also handle command lines (see ``make_bonus.txt``).

Exercise 5B: solving
--------------------

Now write a function that takes such a dictionary and returns a list
of files that have to be generated. To build 'all', the result would be::

	['a.o', 'b.o', 'app', 'all']

Why? To build 'all' we must first build 'app', but to build 'app', we
must first build 'a.o' and 'b.o'. (They in turn depend on 'a.c' and
'b.c' but since are no rules for how to build them, Make assumes they
are existing source files.)

For simplicity, assume that different files won't have common
dependencies (Make handles that smartly, building each file at most
once; you don't have to).

**Hints**:

- This is a classical use case for recursion. There are 2 cases:

- Source files (no rule to build): ``plan('a.c') == []``
- Generated files: ``plan('app') == plan('a.o') + plan('b.o') + ['app']``

**Bonus**: if you also parsed the commands, after computing the plan,
show which commands would be executed.

Solutions: ``make.py``, ``make_bonus.py``
