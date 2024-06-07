#!/usr/bin/python3

import sqlite3 as sql

#always make a connector first
conn = sql.connect('tutorial.db')

#cursor to execute sql queries
cur = conn.cursor()

#create table with column headers. IF TABLE IS CREATED, IT WILL RETURN AN ERROR STATING THE TABLE EXISTS.
# cur.execute(
#     '''CREATE TABLE movie (
#         title text,
#         year INTEGER,
#         score INTEGER
#     )'''
# )

#insert data into table
# cur.execute('''
#     INSERT INTO movie VALUES
#             ('Monty Python and the Holy Grail', 1975, 8.2),
#             ('And Now for Something Completely Different', 1971, 7.5)
# ''')

# conn.commit()

res = cur.execute('SELECT title FROM movie')
print(res.fetchall())

