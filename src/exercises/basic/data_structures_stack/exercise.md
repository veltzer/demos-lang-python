RPN Calculator
==============

A "Reverse Polish Notation" calculator takes input in a strange form,
where operators come after the operands::

	2 2 + 5 *

which means (2 + 2) * 5. There is an extremely simple way to compute
RPN expressions, using a stack:

- When you see a number, push it onto the stack.

- When you see an operator, pop 2 operands from the stack, and push
	the result on the stack.

Write a program that does this, printing the stack after each word::

	[]
	2
	[2.0]
	2
	[2.0, 2.0]
	+
	[4.0]
	5
	[4.0, 5.0]
	*
	[20.0]

**Hints**:

- A list works great to represent a stack - use ``.append(value)`` and
	``.pop()`` methods.

Solution: ``rpn_calculator.py`` (Read this solution! It will teach
you something about using functions in unexpected ways.)
