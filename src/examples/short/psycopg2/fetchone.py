"""
This is an example of how to use the "fetchone" method of the cursor
of psycopg2.

Note:
- the best way to use it is not in a for loop but rather in a while
type loop (see below).

References:
- https://stackoverflow.com/questions/17933344/python-postgres-can-i-fetchall-1-million-rows
"""

import psycopg2

connection_string = "postgresql://localhost/postgres"
with psycopg2.connect(connection_string) as connection:
    cursor = connection.cursor()
    cursor.execute("select * from test")
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
