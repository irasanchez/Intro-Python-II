# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """this class creates objects that represent the user"""

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"Hi, I am {self.name}, and I am in the {self.current_room} area of the room."

    def report_back(self):
        return self.current_room

