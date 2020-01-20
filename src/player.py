# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """this class creates objects that represent the user"""

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"Hi, I am {self.name}."

    def report_back(self):
        return f"I am in {self.location}."

