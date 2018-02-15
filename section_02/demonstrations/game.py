class Character:
    def __init__(self):
        self.strength = 3
        self.health = 10

    def attack(self, other_character):
        other_character.health -= self.strength

    def get_status(self):
        if self.health <= 0:
            return "dead"
        else:
            return "alive"


class Monster(Character):

    def __init__(self):
        self.strength = 6
        self.health = 20


class Game:

    def combat(self, c1, c2):
        no_one_is_dead = True

        while no_one_is_dead:
            c1.attack(c2)
            c2.attack(c1)

            if c1.get_status() == "dead":
                no_one_is_dead = False
            elif c2.get_status() == "dead":
                no_one_is_dead = False


c1 = Character()
c2 = Monster()

g = Game()
g.combat(c1, c2)

print c1.get_status()
print c2.get_status()
