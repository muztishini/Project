import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


class Individual:
    def __init__(self, id: int, full_name: str, passport_number: int):
        self.id = id
        self.full_name = full_name
        self.passport_number = passport_number

    def add_individual(self):
        cursor.execute("INSERT INTO individual (full_name, num_pass) VALUES (?, ?)",
                       (self.full_name, self.passport_number))
        conn.commit()
        conn.close()


class LegalEntity:
    def __init__(self, id: int, inn: int, name: str):
        self.id = id
        self.inn = inn
        self.name = name

    def add_legal(self):
        cursor.execute(
            "INSERT INTO legalentity (name, inn) VALUES (?, ?)",  (self.name, self.inn))
        conn.commit()
        conn.close()


class Customer:
    def __init__(self, id: int, indId: int, leId: int, power: int, consumption: int, connectors: str, dimensions: int, operating_conditions: str):
        self.id = id
        self.indId = indId
        self.leId = leId
        self.power = power
        self.consumption = consumption
        self.connectors = connectors
        self.dimensions = dimensions
        self.operating_conditions = operating_conditions

    def add_customer(self):
        cursor.execute("INSERT INTO customers (indiv_id, legal_id, power, consumption, connectors, dimensions, "
                       "operating_conditions) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (self.indId, self.leId, self.power, self.consumption, self.connectors, self.dimensions, self.operating_conditions))
        conn.commit()
        conn.close()
