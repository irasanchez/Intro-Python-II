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
        return f"Hi, I am {self.name}, and I am in the {self.current_room} area of the room."

    def report_back(self):
        return self.current_room

    def pick_up(self, item_name, item_description):
        self.inventory.append(Item(item_name, item_description))
