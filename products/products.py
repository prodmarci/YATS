import sqlite3

conn = sqlite3.connect(r'd34d-shop\products\db\products.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    description TEXT,
    stock BOOLEAN
)
''')

def list_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    products = []
    
    if rows:
        for row in rows:
            product = {"id": row[0], "name": row[1], "price": row[2], "description": row[3], "in_stock": row[4]}
            products.append(product)
    else:
        print("No products found.")
        
    return(products)
            

def add_product(name, price, description, stock):
    cursor.execute('''
    INSERT INTO products (name, price, description, stock)
    VALUES (?, ?, ?, ?)
    ''', (name, price, description, stock))
    conn.commit()
    print(f"Product '{name}' added successfully.")


def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    print(f"Product with ID {product_id} deleted successfully.")


cursor.execute('SELECT * FROM products')
rows = cursor.fetchall()
for row in rows:
    print(row)