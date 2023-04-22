"""
This is a basic example of how to use the 'texttable' module.

References:
- https://oneau.wordpress.com/2010/05/30/simple-formatted-tables-in-python-with-texttable/
"""

import texttable

table = texttable.Texttable()
header = ['Manager', 'Club', 'Year']
table.header(header)
row = ['Ottmar Hitzfeld', 'Borussia Dortmund, Bayern Munich',\
         '1997 and 2001']
table.add_row(row)
row = ['Ernst Happel', 'Feyenoord, Hamburg', '1970 and 1983']
table.add_row(row)
row = ['Jose Mourinho', 'Porto, Inter Milan', '2004 and 2010']
table.add_row(row)
s = table.draw()
print s
