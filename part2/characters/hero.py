import time
import random
from .character import Character


class Hero(Character):
    def __init__(self):
        super().__init__()
        self.name = 'hero'
        # self.health = 10
        # self.power = 5
        # self.coins = 20

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

    def attack(self, enemy):
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        # 20% of time do double damage
        dice_roll = random.randint(1, 5)
        if dice_roll == 1:
            print("Critical hit!")
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)
        time.sleep(1.5)
