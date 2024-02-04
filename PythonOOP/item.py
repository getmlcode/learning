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
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    def getTotalPrice(self):
        return self.__price*self.quantity

    def applyDiscount(self):
        self.__price = self.__price * self.payRate

    def incrementPrice(self, incrementAmount):
        assert incrementAmount >=0, "increment amount can't be negative"
        self.__price = self.__price + incrementAmount

    def sendEmail(self, message: str):
        self.__connect()
        self.__prepEmailBody()
        self.__send()

    # Private function names begin with __ <double underscore>
    def __connect(self):
        pass
    def __prepEmailBody(self):
        pass
    def __send(self):
        pass

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

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value
