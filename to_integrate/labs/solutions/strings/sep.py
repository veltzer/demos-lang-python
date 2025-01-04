#!/usr/local/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

items = Belgium.split(',')
print('-' * len(Belgium))			    # a)
print(':' . join(items))			    # b)
print(int(items[1]) + int(items[3]))	# c)
print('-' * len(Belgium))			    # d)


"""Well I have this large quantity of string, a hundred and twenty-two 
thousand *miles* of it to be exact, which I inherited. 
Due to bad planning, the hundred and
twenty-two thousand miles is in three inch lengths.  
So it's not very useful.""" 
