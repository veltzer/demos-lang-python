#!/usr/bin/env python

"""
This example shows how to connect to a mysql database using the
'pymysql' module.
"""

import pymysql.cursors
import os.path


# Connect to the database
connection = pymysql.connect(
    host='localhost',
    # user='username',
    # password='password',
    db='test',
    # charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    read_default_file=os.path.expanduser('~/.my.cnf'),
)

connection.close()
