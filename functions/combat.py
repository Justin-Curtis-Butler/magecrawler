#combat.py

import random

from entities.enemy import Enemy
from entities.mage import Mage


def combat(mage: Mage, enemy: Enemy) -> None:
    print(f"\n*** A {enemy.name} attacks! ***")
    while mage.alive and enemy.alive:
        print(f"\n[{mage.name}]\nHP {mage.hp}/{mage.max_hp}\nMana {mage.mana}/{mage.max_mana}\nPortions{mage.potions}")
        for i, s in enumerate(mage.spells, 1):
            print (f" {i}: {s.name} (cost {s.mana_cost}, dmg {s.min_dmg}-{s.max_dmg}")
        print(" m: Meditate (+5 mana)\np: Drink potion (+15 HP)")

        choice = input("> ").strip().lower()

        if choice == "m":
            if mage.mana == mage.max_mana:
                print("You focus but nothing happens")
            else:
                mage.mana = min(mage.max_mana, mage.mana +5)
                print("You focus and regain some ambient mana.")
        elif choice == "p":
            if mage.potions > 0:
                mage.potions -= 1
                if mage.hp == mage.max_hp:
                    print("You wasted a potion!!")
                    continue
                mage.hp = min(mage.max_hp, mage.hp + 15)
                print("You drink a potion. Warmth floods through you.")
            else:
                print("You don't have any potions!")
                continue
        elif choice.isdigit() and 1 <= int(choice) <= len(mage.spells):
            spell = mage.spells[int(choice) - 1]
            if mage.mana < spell.mana_cost:
                print("Not enough mana!")
                continue
            mage.mana -= spell.mana_cost
            dmg = spell.roll()
            if enemy.weakness == spell.name:
                dmg *= 2
                print(f"{enemy.name}: You've found my weakness!")
            enemy.hp -= dmg
            print(f"You cast {spell.name} for {dmg} damage.")
        else:
            print("Invalid choice.")

        if enemy.alive:
            dmg = random.randint(enemy.min_dmg, enemy.max_dmg)
            mage.hp -= dmg
            print(f"The {enemy.name} hits you for {dmg} damage.")

    if mage.alive:
        print(f"\nThe {enemy.name} is defeared!")
