from product import Product
from customer import Customer
import sqlite3


conn = sqlite3.connect('database.db')
cursor = conn.cursor()


def warehouse(power: int, lst: list) -> bool:
    res = False
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE power = ?", (power,))
        cur = cursor.fetchall()
        for item in cur:
            list_result = []
            list_result.append(item[3])
            list_result.append(item[4])
            list_result.append(item[5])
            list_result.append(item[6])
            list_result.append(item[7])

            if list_result == lst:
                res = True
                break

    except TypeError:
        print("Нет такой записи")
    finally:
        conn.close()

    return res


class Employee:
    def __init__(self, id: int, full_name: str, number_phone: int):
        self.id = id
        self.full_name = full_name
        self.number_phone = number_phone
        self.custId = cust.id

    def add_employee(self):
        cursor.execute("INSERT INTO employee (empl_fullname, number_phone, cust_id) VALUES (?, ?, ?)",
                       (self.full_name, self.number_phone, self.custId))
        conn.commit()
        conn.close()


class Order:
    def __init__(self, id: int, payment_type: str):
        self.id = id
        self.custId = cust.id
        self.emplId = empl.id
        self.payment_type = payment_type

    def add_order(self):
        list_cust = []
        list_cust.append(cust.power)
        list_cust.append(cust.consumption)
        list_cust.append(cust.connectors)
        list_cust.append(cust.dimensions)
        list_cust.append(cust.operating_conditions)
        os = warehouse(cust.power, list_cust)
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ordering (payment_type, order_status, cust_id, empl_id) VALUES (?, ?, ?, ?)",
                       (self.payment_type, os, self.custId, self.emplId))
        conn.commit()
        conn.close()

# добавление товара
# pro = Product(1, 4444, 2, 555, 6666, "777", 8888, "lkj")
# pro.add_product()

# создание заказчика
cust = Customer(3, None, 3, 555, 666, "bbb", 4444, "lkj")
cust.add_customer()

# создание сотрудника
empl = Employee(1, "sdf", 123345)
empl.add_employee()

# создание заказа
order = Order(17, "tttt")
order.add_order()


conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM ordering WHERE id = ?", (order.id,))
cur = cursor.fetchone()


print(f"Заказ №{cur[0]}.\nТип оплаты: {cur[3]}.\nХарактеристики заказа: \n " +
      f"Мощность: {cust.power},\n Электропотребление: {cust.consumption},\n Разъемы: {cust.connectors}," +
      f"\n Размеры: {cust.dimensions},\n Условия эксплуатации: {cust.operating_conditions}.\nСтатус заказа: {cur[4]}")

conn.commit()
conn.close()
