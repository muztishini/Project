import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    listId INTEGER,
    cat_id INTEGER,
    power INTEGER,
    consumption INTEGER,
    connectors TEXT,
    dimensions INTEGER,
    operating_conditions TEXT,
    FOREIGN KEY (cat_id) REFERENCES categories(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cat_name TEXT
)
''')

conn.commit()
conn.close()
