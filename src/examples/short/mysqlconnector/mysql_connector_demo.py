"""
This is an example showing how to use the mysql.connector
module to connect and interact with the mysql database.

This module comes from the mysql-connection.
"""

import configparser
import getpass
import os.path

import mysql.connector

'''
get the configuration, including user and password from the ~/.my.cnf
file of the user

if no such file exists then use sensible defaults
'''


def get_config():
    d = {}
    inifile = os.path.expanduser('~/.my.cnf')
    if os.path.isfile(inifile):
        config = configparser.ConfigParser()
        config.read(inifile)
        if config.has_option('mysql', 'user'):
            d['user'] = config.get('mysql', 'user')
        else:
            d['user'] = getpass.getuser()
        if config.has_option('mysql', 'database'):
            d['database'] = config.get('mysql', 'database')
        else:
            d['database'] = 'mysql'
        if config.has_option('mysql', 'password'):
            d['password'] = config.get('mysql', 'password')
        return d
    else:
        d['user'] = getpass.getuser()
        d['database'] = 'mysql'
        return d


db = mysql.connector.Connect(**get_config())
cursor = db.cursor()
cursor.execute('SHOW TABLES')
for row in cursor:
    print(row[0])
# demo with place holders
cursor.execute('SELECT * FROM user WHERE host=%(host)s', {'host': 'localhost'})
for row in cursor:
    print(row)
db.close()
