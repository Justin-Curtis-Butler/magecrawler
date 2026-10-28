#worldbuilder.py

from entities.enemy import Enemy
from entities.mage import Mage
from entities.room import Room
from entities.spell import Spell


def build_dungeon() -> dict[str, Room]:
    return {
        "entrance": Room(
            "Crumbling Entrance",
            "Cold air drifts up from a stairway carved into the rock",
            exits={"north": "hall", "east": "library"},
        ),
        "hall": Room(
            "Hall of Echoes",
            "Your footsteps echo endlessly. Something skitters in the dark.",
            exits={"south": "entrance", "north": "crypt"},
            enemy=Enemy("Giant Rat", 10, 1, 4),
        ),
        "library": Room(
            "Ruined Library",
            "Charred books litter the floor. A potion glints on a shelf.",
            exits={"west": "entrance"},
            loot="potion",
        ),
        "crypt": Room(
            "The Frozen Crypt",
            "Frost coats every surface. A skeletal lich rises to meet you.",
            exits={"south": "hall"},
            enemy=Enemy("Frost Lich", 30, 3, 8, weakness="Fireball"),
        ),
    }

def creat_mage() -> Mage:
    mage = Mage(name="Aldric")
    mage.spells = [
        Spell("Magic Missile", 2, 3, 6),
        Spell("Fireball", 6, 8, 14),
        Spell("Frost Shard", 4, 5, 9),
    ]
    return mage
