#!/usr/bin/python3

import sqlite3 as sq

conn = sq.connect('test.db')
cur = conn.cursor()

# cur.execute(
#     '''CREATE TABLE movies (Title, Year, Score)
# '''
# )

cur.execute(
    '''INSERT INTO movies VALUES
        ('Indiana Jones', 1994, 9.0),
        ('Spiderman', 2007, 9.5)
'''
)
conn.commit()

print(cur.execute('SELECT * FROM movies').fetchall())