# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self,
                 name,
                 description,
                 items=None,
                 n_to="",
                 s_to="",
                 w_to="",
                 e_to=""):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def __str__(self):
        if not self.items:
            return "{self.name}: {self.description} \n There are no items here \n".format(
                self=self)
        output = '{self.name}: {self.description}\n\nItems available here: \n'.format(
            self=self)
        for item in self.items:
            output += f"{item} \n"
        return output
