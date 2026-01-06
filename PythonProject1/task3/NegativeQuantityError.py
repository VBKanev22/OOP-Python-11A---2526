class NegativeQuantityError(Exception):
    def __init__(self, item_name: str, quantity: int):
        message = (
            f"Invalid quantity {quantity} for item '{item_name}'. "
            f"Quantity cannot be negative."
        )
        super().__init__(message)
        self.item_name = item_name
        self.quantity = quantity
