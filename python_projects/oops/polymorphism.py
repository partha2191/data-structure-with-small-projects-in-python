class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr3):
        return self.price > odr3.price

odr1 = Order("Chips", 20)
odr2 = Order("Tea", 15)

print(odr1 > odr2)