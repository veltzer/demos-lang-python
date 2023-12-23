Table
=====

You are given a list of 3 columns, each being a list of strings (all
of the same length)::

	columns = [['H', 'He', 'Li', 'Be'],
		['Hidrogen', 'Helium', 'Litium', 'Berilium'],
		['1.008', '4.003', '6.941', '9.012']]

Your task is to print it as a nice ASCII table.

Exercise 2A: fixed layout
-------------------------

For starters, assume there are exactly 3 columns and print each column
10 characters wide::

	+-------+---------------+-------+
	|H	|Hidrogen	|1.008	|
	+-------+---------------+-------+
	|He	|Helium		|4.003	|
	+-------+---------------+-------+
	|Li	|Litium		|6.941	|
	+-------+---------------+-------+
	|Be	|Berilium	|9.012	|
	+-------+---------------+-------+

This is quite easy. The only tricky part is that the data is arranged
by columns, so you need to access the i'th element of each column in
parallel.

**Hints**:
- ``"-" * 10`` returns ``"----------"``.
- ``"Helium".ljust(10)`` returns ``"Helium "``.
- Try ``zip(columns[0], columns[1], columns[2])`` in the
	interpreter. If you don't understand how this helps you, peek
	at the solution - its an useful function to know!

Solution: ``solution1.py``

Exercise 2B: Auto-fit
---------------------

Now, improve it by computing the proper width for each column::

+--+--------+-----+
|H |Hidrogen|1.008|
+--+--------+-----+
|He|Helium  |4.003|
+--+--------+-----+
|Li|Litium  |6.941|
+--+--------+-----+
|Be|Berilium|9.012|
+--+--------+-----+

This obviously requires doing 2 passes over the data - one to compute
the width for each column, one to print the table.

Solution: ``solution2.py``
