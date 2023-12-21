class ProductCharacter:
    def __init__(self, power: int, consumption: int, connectors: str, dimensions: int, operating_conditions: str):
        self.power = power
        self.consumption = consumption
        self.connectors = connectors
        self.dimensions = dimensions
        self.operating_conditions = operating_conditions


class ConsumerElectronics(ProductCharacter):
    def __init__(self, power: int, consumption: int, connectors: str, dimensions: int, operating_conditions: str, id: int, listId: int):
        super().__init__(power, consumption, connectors, dimensions, operating_conditions)
        self.id = id
        self.listId = listId


class ElectronicComponents(ProductCharacter):
    def __init__(self, power: int, consumption: int, connectors: str, dimensions: int, operating_conditions: str, id: int, listId: int):
        super().__init__(power, consumption, connectors, dimensions, operating_conditions)
        self.id = id
        self.listId = listId


class RadioEngineering(ProductCharacter):
    def __init__(self, power: int, consumption: int, connectors: str, dimensions: int, operating_conditions: str, id: int, listId: int):
        super().__init__(power, consumption, connectors, dimensions, operating_conditions)
        self.id = id
        self.listId = listId
