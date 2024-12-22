import sqlite3
from flask import g

DATABASE = 'calendar.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_db(error=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL CHECK (LENGTH(title) <= 30),
            text TEXT NOT NULL CHECK (LENGTH(text) <= 200)
        )''')
        conn.commit()