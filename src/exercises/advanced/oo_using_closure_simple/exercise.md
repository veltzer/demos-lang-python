# Object Oriented using Closure

Remember: if a function creates a function then the "inner"/"created" function
gets to keep a reference to all of the "outer"/"creator" functions variables.

Another hint:
if a function creates two functions then they both point to the same set of variables.
This is called a "shared closure"

example of a shared closure:

```python
def create_two_functions(x):
    def a():
        pass
    def b():
        pass
    return (a,b)
```

both a and b have a pointer to the SAME X!!!!
That is a "shared closure".

And now for the exercise:
create a `stack`  like data structure without using object oriented programming and
by using only shared closures.

a stack is just a list with two operations: push and pop
