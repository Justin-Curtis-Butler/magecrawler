#room.py

from dataclasses import dataclass, field

from entities.enemy import Enemy


@dataclass
class Room:
    name: str
    description: str
    exits: dict[str, str] = field(default_factory=dict)
    enemy: Enemy | None = None
    loot: str | None = None
