import sqlite3

conn = sqlite3.connect('credentials.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Credentials;

CREATE TABLE Credentials (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    username VARCHAR(50),
    password VARCHAR(50),
    email TEXT,
    fullname TEXT,
    gender TEXT,
    role TEXT
    );
''')

conn.close()
