#showroom.py

from entities.room import Room


def show_room(room: Room) -> None:
    print(f"\n=== {room.name} ===")
    print(room.description)
    print("Exits:", ", ".join(room.exits))
