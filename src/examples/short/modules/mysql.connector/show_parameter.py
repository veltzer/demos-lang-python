""" show_parameter.py """

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
    mycursor = db.cursor()
    mycursor.execute("SELECT @@general_log")
    result = mycursor.fetchone()
    general_log_enabled = result[0]
    print("General log enabled:", general_log_enabled)


if __name__ == "__main__":
    main()
