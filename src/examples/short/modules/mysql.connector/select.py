"""
This is an example showing how to use the mysql.connector
module to select records from a mysql database.

This module comes from the mysql-connection.
"""

import os.path
import mysql.connector


def main():
    option_files = os.path.expanduser("~/.my.cnf")
    option_groups = "clientmyworld"
    db = mysql.connector.connect(
        option_files=option_files,
        option_groups=option_groups,
        database="mysql",
    )
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user WHERE host=%(host)s", {"host": "localhost"})
    for row in cursor:
        for datum in row:
            print(datum)
    db.close()


if __name__ == "__main__":
    main()
