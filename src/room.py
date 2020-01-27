# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    """I am a class that makes rooms in this game"""

    def __init__(self, name, description, items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def __str__(self):
        base_string = f"{self.name}: {self.description}"
        if len(self.items) is not 0:
            base_string += "\n\n👀\nYou see the following items:\n"
            for item in self.items:
                base_string += f"{item.name}: {item.description}\n"

            base_string += "\n\nTo pick up an item, say 'get item1 item2'"
        return base_string
