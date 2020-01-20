# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """this class creates objects that represent the user"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hi, I am {self.name}."

