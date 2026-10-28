#main.py

# Contains the main game loop

from functions.combat import combat
from functions.showroom import show_room
from functions.worldbuilder import build_dungeon, creat_mage


def main() -> None:
    dungeon = build_dungeon()
    mage = creat_mage()
    current = "entrance"
    show_room(dungeon[current])
    print("\nCommands: go <direction>, look, stats, quit")

    while mage.alive:
        room = dungeon[current]
        command = input("\n").strip().lower().split()
        if not command:
            continue
        verb = command[0]

        if verb == "quit":
            print("You flee the dungeon. Farwell.")
            return
        elif verb == "look":
            show_room(room)
        elif verb == "stats":
            print(f"HP {mage.hp}/{mage.max_hp}\nMana {mage.mana}/{mage.max_mana}\nPotions {mage.potions}")
        elif verb == "go" and len(command) > 1:
            direction = command[1]
            if direction not in room.exits:
                print("You can't go that way.")
                continue
            current = room.exits[direction]
            room = dungeon[current]
            show_room(room)

            if room.loot == "potion":
                mage.potions += 1
                room.loot = None
                print("You pick up a healing potion!")

            if room.enemy and room.enemy.alive:
                combat(mage, room.enemy)
        else:
            print("Unknown command.")

    print("\nYou have been overcome... the dungeon claims your loot.\n\nGAME OVER.")


if __name__ == "__main__":
    main()
