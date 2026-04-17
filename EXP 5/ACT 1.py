# A shop inventory dictionary stores item name and quantity. Add new stock.
inventory = {"Apples": 50, "Bananas": 20}
item = "Apples"
added_quantity = 30

if item in inventory:
    inventory[item] += added_quantity  # Adds to existing 50
else:
    inventory[item] = added_quantity   # Creates new entry if not found

print(inventory)


