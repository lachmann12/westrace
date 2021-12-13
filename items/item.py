import emoji
import random

def random_item():
    r = random.random()
    if r < 0.2:
        i = Item("Revolver", 2, 0, 0, 3)
    elif r < 0.4:
        i = Item("Bandana", 0, 1, 0, 1)
    elif r < 0.7:
        i = Item("Boots", 0, 2, 1, 2)
    elif r < 0.8:
        i = Item("Rifle", 4, 0, -1, 3)
    elif r < 0.9:
        i = Item("Vest", 0, 3, 0, 2)
    else:
        i = Item("Eagle", 0, 0, 4, 3)
    return i

class Item:
    name = ""
    damage = 0
    morale = 0
    unit = ""
    cost = 0

    def __init__(self, name, damage, morale, initiative, cost):
      self.name = name
      self.damage = damage
      self.morale = morale
      self.initiative = initiative
      self.cost = cost
    
    def to_str(self):
        damage_str = ""
        morale_str = ""
        init_str = ""
        for i in range(self.damage):
            damage_str = damage_str+emoji.emojize(":star:")
        for i in range(self.morale):
            morale_str = morale_str+emoji.emojize(":green_heart:")
        for i in range(self.initiative):
            init_str = init_str+emoji.emojize(":zzz:")
        
        return "{:<6}".format(self.name)+" "+damage_str+morale_str+init_str