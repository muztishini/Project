import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    power INTEGER,
    consumption INTEGER,
    connectors TEXT,
    dimensions INTEGER,
    operating_conditions TEXT,
    indiv_id INTEGER,
    legal_id INTEGER,
    FOREIGN KEY (indiv_id) REFERENCES individual(id),
    FOREIGN KEY (legal_id) REFERENCES legalentity(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS individual (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    num_pass INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS legalentity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    inn INTEGER
)
''')

conn.commit()
conn.close()
