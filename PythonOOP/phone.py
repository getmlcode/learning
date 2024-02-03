from item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, brokenPhones=0):
        # Call super function to have access to all attributes/methods
        super().__init__(name, price, quantity)

        assert brokenPhones>=0, "brokenPhones arg can't be negative"
        self.brokenPhones = brokenPhones
