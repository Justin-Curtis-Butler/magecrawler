#mage.py

"""Character class definition"""

from dataclasses import dataclass, field

from entities.spell import Spell


@dataclass
class Mage:
    name: str
    max_hp: int = 30
    max_mana: int = 50
    hp: int = 30
    mana: int = 50
    potions: int = 1
    spells: list[Spell] = field(default_factory=list)

    @property
    def alive(self) -> bool:
        return self.hp > 0
