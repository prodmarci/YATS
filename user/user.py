import sqlite3

conn = sqlite3.connect(r'd34d-shop\user\db\language.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    lang TEXT
)
''')

def set_user_language(user_id, lang):
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    
    if cursor.fetchone() is None:
        cursor.execute('''
        INSERT INTO users (user_id, lang)
        VALUES (?, ?)
        ''', (user_id, "langpacks.english"))
    else:
        cursor.execute('''
        UPDATE users
        SET lang = ?
        WHERE user_id = ?
        ''', (lang, user_id))
    conn.commit()
    
def get_user_language(user_id):
    cursor.execute('''
    SELECT lang FROM users WHERE user_id = ?
    ''', (user_id,))
    value = cursor.fetchone()
    
    if value:
        return value[0]
    else:
        set_user_language(user_id, "langpacks.polish")
        return get_user_language(user_id)