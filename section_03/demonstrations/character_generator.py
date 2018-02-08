from random import randint

# character has attributes

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        result = randint(1, self.sides)
        return result


class Attribute:

    def __init__(self, name, short_name, initial_value=0):
        self.name = name
        self.short_name = short_name
        self.value = initial_value

    def gen(self, die_quantity=3, die_sides=6):
        all_rolls = []

        d = Dice(die_sides)

        for n in range(0, die_quantity):
            all_rolls.append(d.roll())

        self.value = sum(all_rolls)

    def __repr__(self):
        return self.short_name + ": " + \
               str(self.value) + \
               "\t B/P: " + \
               str(self.get_bonus()) + \
               "\t(" + \
               self.name + \
               ")"

    def get_bonus(self):
        return (self.value - 10) / 2


class Character:

    def __init__(self):
        self.attribute_list = []

        self.attribute_list.append(Attribute("Strength", "STR"))
        self.attribute_list.append(Attribute("Intelligence", "INT"))
        self.attribute_list.append(Attribute("Dexterity", "DEX"))
        self.attribute_list.append(Attribute("Constitution", "CON"))
        self.attribute_list.append(Attribute("Wisdom", "WIS"))
        self.attribute_list.append(Attribute("Charisma", "CHA"))

    def generate_attributes(self):
        for a in self.attribute_list:
            a.gen(3, 6)

    def show(self):
        for a in self.attribute_list:
            print a


c = Character()
c.generate_attributes()
c.show()
