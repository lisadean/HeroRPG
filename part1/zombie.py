from character import Character

class Zombie(Character):
    def __init__(self):
        self.health = 0
        self.power = 2
        self.name = 'zombie'
        self.immortal = True