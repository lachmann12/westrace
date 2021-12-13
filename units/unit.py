import emoji
from units import unit
import random

def random_unit():
    r = random.random()
    if r < 0.1:
        i = Unit("Cow", 1, 3, 2, 0, 1)
    elif r < 0.2:
        i = Unit("Cowboy", 2, 1, 2, 1, 2)
    elif r < 0.3:
        i = Unit("Sherrif", 3, 2, 2, 2, 2)
    elif r < 0.4:
        i = Unit("Bandit", 3, 1, 3, 3, 2)
    elif r < 0.5:
        i = Unit("Apache", 4, 2, 3, 1, 2)
    elif r < 0.6:
        i = Unit("Banker", 1, 1, 4, 0, 2)
    elif r < 0.7:
        i = Unit("Bar Keeper", 1, 1, 4, 0, 2)
    elif r < 0.8:
        i = Unit("Piano Man", 2, 3, 4, 0, 2)
    elif r < 0.85:
        i = Unit("Madame", 2, 2, 4, 0, 2)
    elif r < 0.9:
        i = Unit("Pharmacist", 1, 1, 4, 0, 2)
    else:
        i = Unit("Shaman", 1, 1, 4, 0, 2)
    return i

class Unit:
    name = "unnamed"
    damage = ""
    morale = ""
    cost = ""
    max_equip = 0
    initiative = 0
    level = 1

    equipment = []

    def __init__(self, name, damage, morale, cost, max_equip, initiative):
        self.name = name
        self.damage = damage
        self.morale = morale
        self.cost = cost
        self.max_equip = max_equip
        self.initiative = initiative
        self.equipment = []

    def to_str(self):
        out = "{:<10}".format(self.name)+" "+emoji.emojize(":green_heart:")+str(self.morale)+" "+emoji.emojize(":star:")+str(self.damage)+" "+emoji.emojize(":zzz:")+str(self.initiative)
        for e in self.equipment:
           out = out+" | "+e.to_str()
        return out

    def equip(self, item):
        print(self.name+" - "+item.name)
        if len(self.equipment) < self.max_equip:
            self.equipment.append(item)
            self.damage += item.damage
            self.morale += item.morale
            self.initiative += item.initiative
