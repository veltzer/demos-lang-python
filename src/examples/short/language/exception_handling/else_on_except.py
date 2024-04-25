"""
This example shows that you can write an "else" block on try statements.

Here is the difference between "finally" and "else":
- the "finally" block exectuted in any case, both if an exception was thrown or not.
- the "else" block gets executed only if no exceptions were raised.

Why do you need this feature?
So you would be able to put in a piece of code that will be executed only in case
there were no exceptions.

technical notes:
- if you want to use "else" and "finally" together "else" should come before "finally".
"""

import random


try:
    if random.random() < 0.5:
        print("in raise")
        raise ValueError("hello")
except ValueError:
    print("in except")
else:
    print("in else")
finally:
    print("in finally")
