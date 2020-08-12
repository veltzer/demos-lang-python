"""
A basic program that connects to a postgresql database using the psycopg2 module

Notes:
- we do not supply a username here since we assume we will run this script as
a UNIX user whose name is also a valid postgres user name.
- we do not supply a password here since we connect to 'localhost' and postgresql
comes with a default configuration (pg_hba.conf) that states that connections
from local host are authenticated using the operating system user name and
with no password.
"""

import psycopg2

connection_string = "postgresql://localhost/postgres"
with psycopg2.connect(connection_string) as connection:
    cursor = connection.cursor()
    cursor.execute("select VERSION()")
    row = cursor.fetchone()
    print(row)
