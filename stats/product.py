import sqlite3

conn = sqlite3.connect(r'd34d-shop\stats\db\stats.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS product_visits (
        item_id INTEGER PRIMARY KEY,
        visits INTEGER
    )
''')

def increment_visits(item_id):
    c.execute("SELECT visits FROM product_visits WHERE item_id = ?", (item_id,))
    result = c.fetchone()

    if result is None:
        c.execute("INSERT INTO product_visits (item_id, visits) VALUES (?, ?)", (item_id, 1))
    else:
        c.execute("UPDATE product_visits SET visits = visits + 1 WHERE item_id = ?", (item_id,))
        
    conn.commit()