import random
from .character import Character


class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 5
        self.coins = 20

    def heal_damage(self, points):
        self.health += points
        print("%s healed %d points." % (self.name, points))

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))

        # 20% of time heal for 2 points
        dice_roll = random.randint(1, 5)
        if dice_roll == 1:
            self.heal_damage(2)

        if self.health <= 0:
            print("%s is dead." % self.name)
