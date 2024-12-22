from .database import get_db

def create_event(date, title, text):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO events (date, title, text) VALUES (?, ?, ?)', (date, title, text))
    db.commit()
    return cursor.lastrowid

def get_events():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM events')
    return cursor.fetchall()

def get_event(event_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
    return cursor.fetchone()

def update_event(event_id, title, text):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('UPDATE events SET title = ?, text = ? WHERE id = ?', (title, text, event_id))
    db.commit()
    return cursor.rowcount

def delete_event(event_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM events WHERE id = ?', (event_id,))
    db.commit()
    return cursor.rowcount
