- write a function called: is_prime
	This function accepts a single number and returns whether it is prime or not.

- now we want to speed up function and add a cache.
	The idea is that if we even calculate is_prime(n) for a certain n, we *NEVER*
	want to calculate this again.

	write a decorator called "cache".
	you will use it this way:

	@cache
	def is_prime(n):
		...

	The decorate will save the results of the calculation and will never call
	the function for integers for which it already calculated if they are prime or not.

- BONUS: make your decorator work for more than one function
