"""
This example shows how to connect to a mysql database using the
"pymysql" module.
"""

import os.path

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    # user="username",  # noqa: ERA001  teaching: kept in the comment for the reader
    # password="password",  # noqa: ERA001  teaching: kept in the comment for the reader
    db="test",
    # charset="utf8mb4",  # noqa: ERA001  teaching: kept in the comment for the reader
    cursorclass=pymysql.cursors.DictCursor,
    read_default_file=os.path.expanduser("~/.my.cnf"),
)

connection.close()
