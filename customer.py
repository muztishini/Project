from product import ProductCharacter
from typing import List


class Individual:
    def __init__(self, id: int, full_name: str, passport_number: int):
        self.id = id
        self.full_name = full_name
        self.passport_number = passport_number


class LegalEntity:
    def __init__(self, id: int, inn: int, name: str):
        self.id = id
        self.inn = inn
        self.name = name


class Customer(ProductCharacter):
    def __init__(self, id: int, indId: int, leId: int, prod_char: List[ProductCharacter]):
        self.id = id
        self.indId = indId
        self.leId = leId
        self.prod_char = prod_char
