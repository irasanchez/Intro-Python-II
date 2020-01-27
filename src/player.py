# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player:
    """I am a class that creates the user's player in this game"""

    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"Hi, I am {self.name}, and I am located {self.current_room}."

    def report_back(self):
        return "▶▶▶ You are here: " + str(self.current_room)

    def pick_up(self, item):
        self.inventory.append(Item(item.name, item.description))
        print(f"\n(͡° ͜ʖ ͡°)\n\nPicked up {item.name}.")
        self.current_room.items.remove(item)

    def drop(self, item_to_drop):
        for item in self.inventory:
            if item.name.lower() == item_to_drop:
                self.inventory.remove(item)
                print(f"\n(͡° ͜ʖ ͡°)\n\nDropped {item.name}.")
