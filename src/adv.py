#from file import function
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("What is your name?")
current_player = Player(name, room["outside"])
print(current_player.location)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(f"player is in {current_player.location.name}")
    print(current_player.location.name)
    user_input = input(
        "Pick a cardinal direction -- n, s, e, w. Press q to quit.").lower()

    if user_input == 'n' and current_player.location.name != 'Grand Overlook' and current_player.location.name != 'Treasure Chamber':
        current_player.location = current_player.location.n_to
    elif user_input == 's' and current_player.location.name != 'Narrow Passage' and current_player.location.name != 'Outside Cave Entrance':
        current_player.location = current_player.location.s_to
    elif user_input == 'e' and current_player.location.name != 'Narrow Passage' and current_player.location.name != 'Treasure Chamber' and current_player.location.name != 'Grand Overlook' and current_player.location.name != 'Outside Cave Entrance':
        current_player.location = current_player.location.e_to
    elif user_input == 'w' and current_player.location.name != 'Foyer' and current_player.location.name != 'Outside Cave Entrance' and current_player.location.name != 'Grand Overlook' and current_player.location.name != 'Treasure Chamber':
        current_player.location = current_player.location.w_to
    elif user_input == 'q':
        print("Game Over!")
    else:
        print("Please enter a valid direction (n, s, e, w) or q to quit")