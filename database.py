import sqlite3

conn = sqlite3.connect('credentials.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Credentials;

CREATE TABLE Credentials (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email TEXT NOT NULL,
    fullname TEXT NOT NULL,
    gender TEXT NOT NULL,
    role TEXT NOT NULL
    );
''')

conn.close()
