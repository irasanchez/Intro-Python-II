# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=None):
        self.location = location
        self.name = ""
        self.items = items

    def __str__(self):
        return 'I am in {self.location}'.format(self=self)
