from task3.OutOfStockError import OutOfStockError
from task3.NegativeQuantityError import NegativeQuantityError

class Store:
    def __init__(self):
        self.available_items = {}

    def add_item(self, item_name: str, quantity: int):
        self.available_items[item_name] = self.available_items.get(item_name, 0) + quantity

    def purchase_item(self, item_name: str, quantity: int):
        if quantity < 0:
            raise NegativeQuantityError(item_name, quantity)

        available_quantity = self.available_items.get(item_name, 0)

        if available_quantity < quantity:
            raise OutOfStockError(item_name, quantity, available_quantity)

        self.available_items[item_name] = available_quantity - quantity
        print(f"Successfully purchased {quantity} of '{item_name}'. Remaining: {self.available_items[item_name]}")
