"""
This example shows how to use the 'fetchmany' api of the cursor of psycopg2.

References:
- https://www.python.org/dev/peps/pep-0249/#arraysize
- https://stackoverflow.com/questions/17933344/python-postgres-can-i-fetchall-1-million-rows
"""

import psycopg2

connection_string = "postgresql://localhost/postgres"
with psycopg2.connect(connection_string) as connection:
    cursor = connection.cursor()
    print(cursor.arraysize)
    cursor.arraysize = 3
    cursor.execute("select * from test")
    while True:
        print('loop')
        rows = cursor.fetchmany()
        if not rows:
            break
        for row in rows:
            print(row)
