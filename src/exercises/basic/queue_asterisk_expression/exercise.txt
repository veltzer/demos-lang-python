Start with an empty queue.
you are given an expression of asterisks and letters.
When you see an asterisk, remove from the queue.
When you see a letter, add it to the queue
Show the state of the queue when the expression is over.

* check that the input is valid (only single letters or asterisk)

Examples:
	"A B C" -> ABC
	"a b c d *" -> bcd
	"F O O M * A * R * K" -> "MARK"
