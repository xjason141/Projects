#!/usr/bin/python3

#store login info in db using sqlite
import sqlite3 as sq
import hashlib

conn = sq.connect('gui/info.db')
cur = conn.cursor()

# #creates db if one doesnt already exists
cur.execute('''
    CREATE TABLE IF NOT EXISTS loginInfo (
            id INTEGER PRIMARY KEY,
            user VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL 
            )
''')

#set username and password
user1, pass1 = 'didi123', hashlib.sha256('didipassword'.encode()).hexdigest()

# insert info into table
# cur.execute('INSERT INTO loginInfo (user, password) VALUES (?, ?)', (user1, pass1))
# conn.commit()

