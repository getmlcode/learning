import json 
import csv

class Item(object):
    payRate = 0.8 # class attribute
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # quantity is expcted to be int as it is assigned 
        # to int in the argument
        assert price>=0, "price arg can't be negative"
        assert quantity>=0, "quantity arg can't be negative"

        # Assign values to object attrib
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def getTotalPrice(self):
        return self.price*self.quantity

    def applyDiscount(self):
        self.price = self.price * self.payRate

    @classmethod
    def instantiateFromCsv(cls):
        # receives class reference as first argument
        with open("PythonOOP\\data.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")))
    
    @staticmethod
    def isInteger(num):
        # receives regular argument, not an instance, like regular function
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        pass

    def __repr__(self):
        # Returning string to represent this object
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        #return json.dumps(self.__dict__)
