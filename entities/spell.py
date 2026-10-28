#spell.py

import random
from dataclasses import dataclass


@dataclass
class Spell:
    name: str
    mana_cost: int
    min_dmg: int
    max_dmg: int

    def roll(self) -> int:
        return random.randint(self.min_dmg, self.max_dmg)
