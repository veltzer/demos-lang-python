import csv
import sqlite3


def read_csv(filename):
    """Generate dictionaries, drop the descriptions."""
    with open(filename) as f:
        for date, package, version, _description in csv.reader(f):
            yield {"date": date, "package": package, "version": version}


db = sqlite3.connect("pypi.sqlite")
cursor = db.cursor()
with db:
    cursor.execute("DROP TABLE IF EXISTS pypi")  # ensure a clean start
    cursor.execute("CREATE TABLE pypi (date, package, version)")
    # noinspection SqlResolve
    cursor.executemany(
        "INSERT INTO pypi VALUES (:date, :package, :version)", read_csv("pypi.csv"))

# test results
# noinspection SqlResolve
cursor.execute("SELECT * FROM pypi")
for row in cursor:
    print(row)
