#enemy.py

from dataclasses import dataclass


@dataclass
class Enemy:
    name: str
    hp: int
    min_dmg: int
    max_dmg: int
    weakness: str | None = None

    @property
    def alive(self) -> bool:
        return self.hp > 0
