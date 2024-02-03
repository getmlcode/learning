from item import Item
from phone import Phone

if __name__=="__main__":

    item1 = Item("phone", 100, 4)
    print(type(item1))
    print(item1.name)
    print(item1.getTotalPrice())

    item2 = Item("laptop", 1000, 4)
    item2.hasNumPad = False
    print(type(item2))
    print(item2.name)
    print(item2.getTotalPrice())

    print(Item.payRate)
    print(item1.payRate) # gets attrib from class level as it is not found at instance level
    print(item2.payRate)

    #print(Item.__dict__)
    #print(item1.__dict__)
    #print(item2.__dict__)

    item1.applyDiscount()
    print(item1.price)

    item2.payRate = 0.7
    item2.applyDiscount()
    print(item2.price)

    phone1 = Phone("phonev10",45,2,1)
    print(phone1.getTotalPrice())

    print(Item.all)
    print(Phone.all)
