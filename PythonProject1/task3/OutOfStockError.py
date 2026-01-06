class OutOfStockError(Exception):
    def __init__(self, item_name: str, requested_quantity: int, available_quantity: int):
        message = (
            f"Cannot purchase {requested_quantity} of '{item_name}'. "
            f"Only {available_quantity} available."
        )
        super().__init__(message)
        self.item_name = item_name
        self.requested_quantity = requested_quantity
        self.available_quantity = available_quantity
