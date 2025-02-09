import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect(r'd34d-shop\stats\db\stats.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS bot_visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL UNIQUE,
        date TEXT NOT NULL
    )
''')

def add_user(user_id):
    date = datetime.now().strftime("%Y-%m-%d")
    c.execute("SELECT date FROM bot_visits WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    
    if result:
        existing_date = result[0]
        if existing_date < date:
            c.execute("UPDATE bot_visits SET date = ? WHERE user_id = ?", (date, user_id))
    else:
        c.execute("INSERT INTO bot_visits (user_id, date) VALUES (?, ?)", (user_id, date))
    
    conn.commit()

def get_user_count(days):
    date_from = (datetime.now() - timedelta(days=days - 1)).strftime("%Y-%m-%d")
    c.execute("SELECT COUNT(*) FROM bot_visits WHERE date >= ?", (date_from,))
    return c.fetchone()[0]