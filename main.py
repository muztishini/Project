from product import ConsumerElectronics, ElectronicComponents, RadioEngineering
from customer import Customer


class Warehouse:
    def __init__(self, id: int):
        self.id = id
        self.ceId = ce.id
        self.ecId = ec.id
        self.reId = re.id


class Employee:
    def __init__(self, id: int, full_name: str, number_phone: int):
        self.id = id
        self.full_name = full_name
        self.number_phone = number_phone
        self.custId = cust.id
        self.prod_char = cust.prod_char


class Order:
    def __init__(self, id: int, payment_type: int, order_status: bool):
        self.id = id
        self.custId = cust.id
        self.emplId = empl.id
        self.payment_type = payment_type
        self.order_status = order_status
        self.prod_char = empl.prod_char


ce = ConsumerElectronics(100, 55, "vbn", 6, "mnb", 1, 666)
ec = ElectronicComponents(200, 44, "ccc", 7, "ffff", 5, 777)
re = RadioEngineering(300, 33, 4, "asd", 54321, 9, 888)
cust = Customer(1, 2, 3, [100, 55, "vbn", 6, "mnb"])
empl = Employee(1, "sdf", 123345)
wh = Warehouse(2)
# print(wh.ecId)

if wh.ceId == 1:
    list_prod_char = []
    list_prod_char.append(ce.power)
    list_prod_char.append(ce.consumption)
    list_prod_char.append(ce.connectors)
    list_prod_char.append(ce.dimensions)
    list_prod_char.append(ce.operating_conditions)
    str_prod_char = "Бытовая электроника: "
# if wh.ecId == 5:
#     list_prod_char = []
#     list_prod_char.append(ec.power)
#     list_prod_char.append(ec.consumption)
#     list_prod_char.append(ec.connectors)
#     list_prod_char.append(ec.dimensions)
#     list_prod_char.append(ec.operating_conditions)
#     str_prod_char = "Электронные компоненты: "

if empl.prod_char == list_prod_char:
    os = True
else:
    os = False

order = Order(1, 2, os)
print(f"Заказ №{order.id}.\nТип оплаты: {order.payment_type}.\nХарактеристики заказа: {str_prod_char}\n "+
      f"Мощность: {empl.prod_char[0]},\n Электропотребление: {empl.prod_char[1]},\n Разъемы: {empl.prod_char[2]},"+
      f"\n Размеры: {empl.prod_char[3]},\n Условия эксплуатации: {empl.prod_char[4]}.\nСтатус заказа: {order.order_status}")
