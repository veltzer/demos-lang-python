Write a synchronized (thread safe) stack.
The API:
	Push(self,x)
	Pop(self)
Any thread could push or pop from the stack.
- in the first variant a pop from an empty stack simply
	returns.
- in the second variant a pop from an empty stack sleeps
	until data is available.

Write a script that will run 3 producer threads, which will put numbers up to 20 in the stack, and 3 consumer threads which will pop letters from the stack.
