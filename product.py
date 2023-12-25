import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


class Category:
    def __init__(self, catId, cat_name):
        self.catId = catId
        self.cat_name = cat_name


class Product:
    def __init__(self, id: int, listId: int, catId: int, power: int, consumption: int,
                 connectors: str, dimensions: int, operating_conditions: str):
        self.id = id
        self.listId = listId
        self.cat_id = catId
        self.power = power
        self.consumption = consumption
        self.connectors = connectors
        self.dimensions = dimensions
        self.operating_conditions = operating_conditions

    def add_product(self):
        cursor.execute("INSERT INTO products (listId, cat_id, power, consumption, connectors, dimensions, "
                       "operating_conditions) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (self.listId, self.cat_id, self.power, self.consumption, self.connectors, self.dimensions, self.operating_conditions))
        conn.commit()
        conn.close()
