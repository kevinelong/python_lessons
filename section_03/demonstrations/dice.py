from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        result = randint(1, self.sides)
        return result


class Roller:
    value = 0

    def __init__(self):
        pass

    def gen(self, die_quantity=3, die_sides=6):
        all_rolls = []

        d = Dice(die_sides)

        for n in range(0, die_quantity):
            all_rolls.append(d.roll())

        self.value = sum(all_rolls)

    def best_x_out_of_y(self, x=3, y=5, die_sides=6):
        all_rolls = []
        d = Dice(die_sides)

        for n in range(0, y):
            all_rolls.append(d.roll())
        all_rolls.sort()
        all_rolls.reverse()
        best_rolls = all_rolls[0:x]
        self.value = sum(best_rolls)


r = Roller()
r.best_x_out_of_y()
print r.value
