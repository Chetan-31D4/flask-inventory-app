import sqlite3
conn = sqlite3.connect('inventory.db')
conn.execute("INSERT INTO products (name, quantity) VALUES ('Test product', 10 )")
conn.commit()
conn.close()
print("Database and table created.")