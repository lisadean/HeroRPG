from characters import Hero, Wizard, Goblin
from battle import Battle
from store import Store


hero = Hero()
enemies = [Goblin(), Wizard()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
