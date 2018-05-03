import random
from .character import Character


class Shadow(Character):
    def __init__(self):
        super().__init__()
        self.name = 'shadow'
        self.health = 1

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

    def receive_damage(self, points):
        dice_roll = random.randint(1, 10)
        if dice_roll == 1:
            self.health -= points
            print("%s received %d damage." % (self.name, points))
        else:
            print("%s evaded %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)
