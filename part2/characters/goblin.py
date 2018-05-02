from .character import Character


class Goblin(Character):
    def __init__(self):
        super().__init__()
        self.name = 'goblin'
        self.health = 6
        self.power = 2
