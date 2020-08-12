import moda1
import modb1

# lets call the regular version of the function
print('before hacking')
modb1.funcb1()

# lets patch
print('after hacking')


def hacked1():
    print('hacked1')


moda1.funca1 = hacked1
modb1.funcb1()

import modb2
import moda2

# lets call the regular version of the function
print('before hacking')
modb2.funcb2()

# lets patch
print('after hacking')


def hacked2():
    print('hacked2')


moda2.funca2 = hacked2
modb2.funcb2()

print('mmm, didnt work. Trying to patch modb directly')
modb2.funca2 = hacked2
modb2.funcb2()
