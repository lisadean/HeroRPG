class Character(object):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.name = '<undefined>'
        self.immortal = False

    def attack(self, enemy):
        enemy.health -= self.power
        print("The %s attacks and does %d damage to the %s." % (self.name, self.power, enemy.name))
        if (enemy.health <= 0 and not enemy.immortal):
            print("The %s is dead." % (enemy.name))
    
    def alive(self):
        return (self.health > 0 or self.immortal)

    def print_status(self):
        if self.immortal:
            print("The %s is immortal and has %d power." % (self.name, self.power))
        else:
            print("The %s has %d health and has %d power." % (self.name, self.health, self.power))