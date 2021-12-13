from units import unit
from items import item
import time

going = True
coins = 10

player_score = 0
player_round = 0

n_shop_items = 2
n_shop_units = 4
n_roster = 5

roster = []
for i in range(n_roster):
    roster.append(0)

shop_units = []
shop_items = []

shop_units = []
for i in range(n_shop_units):
    shop_units.append(unit.random_unit())

shop_items = []
for i in range(n_shop_items):
    shop_items.append(item.random_item())

print("Coins: "+str(coins))

while going:
    time.sleep(0.1)
    action = input("Action: ")
    if action == "q":
        print("Exit")
        going = False
    elif action == "u":
        myunit = unit.Unit("Cow", 2, 3, 5, 2)
        print(myunit.to_str())
    elif action == "i":
        myitem = item.Item("Revolver", 3, 1, 0, 3)
        print(myitem.to_str())
    elif action == "rsi":
        shop_items = []
        for i in range(n_shop_items):
            shop_items.append(item.random_item())
    elif action == "rsu":
        shop_units = []
        for i in range(n_shop_units):
            shop_units.append(unit.random_unit())
    elif action == "lsi":
        for i in range(len(shop_items)):
            if shop_items[i] == 0:
                print("  - "+str(i)+" empty")
            else:
                print("  - "+str(i)+" "+shop_items[i].to_str())
    elif action == "lsu":
        for i in range(len(shop_units)):
            if shop_units[i] == 0:
                print("  - "+str(i)+" empty")
            else:
                print("  - "+str(i)+" "+shop_units[i].to_str())
    elif action == "r":
        for i in range(n_roster):
            if roster[i] != 0:
                print(str(i)+" "+roster[i].to_str())
            else:
                print(str(i)+" empty")
    elif action == "c":
        print("Coins: "+str(coins))
    elif action == "bi":
        print("Item store")
        for i in range(len(shop_items)):
            if shop_items[i] == 0:
                print("  - "+str(i)+" empty")
            else:
                print("  - "+str(i)+" "+shop_items[i].to_str())
        item_buy = input("Buy item: ")
        if item_buy == "q":
            continue
        elif shop_items[int(item_buy)] != 0:
            if int(item_buy) >= 0 and int(item_buy) < len(shop_items) and coins >= shop_items[int(item_buy)].cost:
                for i in range(n_roster):
                    if roster[i] != 0:
                        print(str(i)+" "+roster[i].to_str())
                    else:
                        print(str(i)+" empty")
                action = int(input("Equip: "))
                if roster[action] != 0:
                    coins -= shop_items[int(item_buy)].cost
                    print("equip")
                    roster[action].equip(shop_items[int(item_buy)])
                    shop_items[int(item_buy)] = 0
    elif action == "bu":
        print("Unit store")
        for i in range(len(shop_units)):
            if shop_units[i] == 0:
                print("  - "+str(i)+" empty")
            else:
                print("  - "+str(i)+" "+shop_units[i].to_str())
        unit_buy = input("Buy unit: ")
        if unit_buy == "q":
            continue
        elif int(unit_buy) >=0 and int(unit_buy) < len(shop_units) and coins >= shop_units[int(unit_buy)].cost:
            for i in range(n_roster):
                if roster[i] != 0:
                    print(str(i)+" "+roster[i].to_str())
                else:
                    print(str(i)+" empty")
            action = int(input("Place: "))
            if roster[action] == 0:
                coins -= shop_units[int(unit_buy)].cost
                roster[action] = shop_units[int(unit_buy)]
                shop_units[int(unit_buy)] = 0
        
        



