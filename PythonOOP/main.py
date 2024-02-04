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

    item1.applyDiscount()
    print(item1.price)

    item2.payRate = 0.7
    item2.applyDiscount()
    print(item2.price)

    phone1 = Phone("phonev10",45,2,1)
    print(phone1.getTotalPrice())

    print(Item.all)
    print(Phone.all)
    #print(Item.__dict__)
    #print(item1.__dict__)
    #print(item2.__dict__)
    
    # ------------------getter and setter--------------------------

    item3 = Item("MyItem", 100, 4)
    #item3.readOnlyName = "aa" # will throw error, can't set attribute
    print(item3.name) # name is property and returns __name
    #print(item3.__name) # throws error : no attribute __name
    #item3.__name = "changedName" # adds accesible attribute __name
    item3.name = "newName" # throws error if setter for name is absent
    print(item3.name) # name is property and returns __name

    print(item3.__dict__)
    print(item3._Item__name)
    #item3._Item__name = "hh" # this changes the property name
    print(item3._Item__name) 
    print(item3.name)
    print(item3.price)
    item3.applyDiscount()
    print(item3.price)
    item3.incrementPrice(54)
    print(item3.price)

    #item3.price = 600 # throws error as we don't keep setter for price to avoid direct manipulation

    item3.sendEmail("ss")
