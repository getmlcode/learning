from item import Item
import json

Item.instantiateFromCsv()
print(Item.all)
print(Item.isInteger(7))
print(Item.isInteger(7.5))
print(Item.isInteger(7.0))

for item in Item.all:
    print(json.dumps(item.__dict__))