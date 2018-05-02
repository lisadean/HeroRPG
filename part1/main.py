"""
In this simple RPG game, the hero fights the enemy. He has the options to:

1. fight enemy
2. do nothing - in which case the enemy will attack him anyway
3. flee

"""
from hero import Hero
from goblin import Goblin
from zombie import Zombie

def main():
    enemy = Goblin()
    hero = Hero()

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        response = input()
        if response == "1":
            # Hero attacks enemy
            hero.attack(enemy)
        elif response == "2":
            pass
        elif response == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % input)

        if enemy.alive():
            # enemy attacks hero
            enemy.attack(hero)

main()
