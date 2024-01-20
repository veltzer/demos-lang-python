"""
An example of how to create an sqlite3 database using python
"""


import sqlite3
import os
import tempfile

# Create a temporary file in /tmp
with tempfile.NamedTemporaryFile(suffix='.db', dir='/tmp', delete=True) as db_file:
    # Connect to the database
    conn = sqlite3.connect(db_file.name)

    # Create a table
    conn.execute("CREATE TABLE temp_table (id INTEGER PRIMARY KEY, name TEXT, value REAL)")

    # Insert some data
    conn.execute("INSERT INTO temp_table VALUES (1, 'data', 10.5)")

    # Save and close
    conn.commit()
    conn.close()

    # Verify the database exists in /tmp
    assert os.path.exists(db_file.name)
