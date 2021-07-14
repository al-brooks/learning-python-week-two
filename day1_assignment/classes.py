class Store:
    def __init__(self, store, address = "1200 Lakeview Ave"):
        self.name = store
        self.address = address
        self.items = []

class Grocery:
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.total = f"{product}, Quantity: {quantity} Units, Total Price: ${price * quantity}"
