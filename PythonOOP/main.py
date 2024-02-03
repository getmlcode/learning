class Item(object):
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getTotalPrice(self):
        return self.price*self.quantity

item1 = Item("phone", 100, 4)

print(type(item1))
print(item1.name)
print(item1.getTotalPrice())

item2 = Item("laptop", 1000, 4)
item2.hasNumPad = False

print(type(item2))
print(item2.name)
print(item2.getTotalPrice())

item3 = Item("laptop", 1000)

print(type(item3))
print(item3.name)
print(item3.getTotalPrice())