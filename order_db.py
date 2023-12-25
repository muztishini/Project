import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cust_id INTEGER,
    empl_fullname TEXT,
    number_phone INTEGER,
    FOREIGN KEY (cust_id) REFERENCES customers(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ordering (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cust_id INTEGER,
    empl_id INTEGER,
    payment_type TEXT,
    order_status BLOB,
    FOREIGN KEY (cust_id) REFERENCES customers(id),
    FOREIGN KEY (empl_id) REFERENCES employee(id)
)
''')

conn.commit()
conn.close()
