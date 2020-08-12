"""
This example shows how to use the 'fetchall' api of the cursor of psycopg2.

Notes:
- do not use this API when you are bringing a lot of records from the database.

References:
- https://www.python.org/dev/peps/pep-0249/#arraysize
- https://stackoverflow.com/questions/17933344/python-postgres-can-i-fetchall-1-million-rows
"""

import psycopg2

connection_string = "postgresql://localhost/postgres"
with psycopg2.connect(connection_string) as connection:
    cursor = connection.cursor()
    cursor.execute("select * from test")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
