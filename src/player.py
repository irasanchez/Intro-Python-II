# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, inventory=[]):
        self.location = location
        self.name = ""
        self.inventory = inventory

    def __str__(self):
        return 'Name: {self.name}.\nLocation: {self.location}\nInventory: '.format(
            self=self)
