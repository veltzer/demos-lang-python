#! /usr/bin/python
# Python 3 version

import math
import decimal

class Frange:

    def __init__ (self, start, stop=None, step=0.25):
        self.step = decimal.Decimal(str(step))

        if stop is None:
            self.stop = decimal.Decimal(str(start))
            self.start = decimal.Decimal(0)
        else: 
            self.stop = decimal.Decimal(str(stop))
            self.start = decimal.Decimal(str(start))

        # Calculate length
        if self.step == 0:
            self.len = 0
        else:
            self.len = math.ceil((self.stop - self.start)/self.step)
            if self.len < 0: self.len = 0


    def __len__(self):
        return self.len

    def __getitem__(self, index):

        if index < 0:
            index = self.len + index
        
        if index >= self.len or index < 0:
            raise IndexError("index out of range")

        item = self.start + (index * self.step)
        return item
   
    def __repr__(self):
        retn = (f"{self.__class__.__name__:}({float(self.start):},"
                + f" {float(self.stop):}, {float(self.step):})")
        return retn
  

    def __eq__(self, rhs):
        if (self.start == rhs.start and
              self.stop  == rhs.stop  and
              self.step  == rhs.step):
            return True
        else:
            return False
        

    def __iter__(self):
        # Will return None on an empty list.
        if self.step != 0:         
            curr = self.start
            while curr < self.stop:
                yield float(curr)
                curr += self.step

        
if __name__ == "__main__":
    def printit(r):
        print(r, len(r), list(r))

    printit(Frange(1.1, 3))
    printit(Frange(1, 3, 0.33))
    printit(Frange(1, 3, 1))
    printit(Frange(3, 1))
    printit(Frange(-1, -0.5, 0.1))
    printit(Frange(1, 3, 0))   # Should return None.

    res = []
    for num in Frange(3.142, 12):
        res.append(f"{num:05.2f}")
    print(" ".join(res))

    one = list(Frange(0, 3.5, 0.25))
    two = list(Frange(3.5))
    if one == two:
        print("Defaults worked!")
    else:
        print("Oops!  Defaults did not work")
        print("one:", one)
        print("two:", two)

    one = Frange(3.3, 8.5)
    two = Frange(3.3, 8.5)

    if one == two:
        print("Equality worked!")
    else:
        print("Failed equality")

    if one != two:
        print("Failed Inequality")
    else:
        print("Inequality worked!")

    print()
    print(list(one))
    print(one[2])
    print(one[-1])
    print(one[-3])

    try:
        print(one[len(one)])   # Should crash.
    except IndexError as err:
        print(err)

    try:
        print(one[-len(one) - 1])
    except IndexError as err:
        print(err)



