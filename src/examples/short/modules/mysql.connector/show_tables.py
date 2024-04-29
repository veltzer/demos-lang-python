"""
This is an example showing how to use the mysql.connector
module to connect and interact with the mysql database.

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
    )
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    for row in cursor:
        for datum in row:
            print(datum)
    db.close()


if __name__ == "__main__":
    main()
