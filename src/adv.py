from room import Room
from player import Player
from item import Item

items = {
    "dagger": Item("Dagger", "A pointy, stabby thing"),
    "mint": Item("Mint", "A complimentary mint. And, it's peppermint!"),
    "lipstick": Item("Lipstick", "I feel prettyyy!! Oh so prettyyy!!"),
    "mirror": Item("Mirror", "The Mirror  of Morbidity, specifically... We all die some day...")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["dagger"]]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [items["mirror"]]),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", [items["lipstick"]]),
}


# Link rooms together
# saves an area (instance of Room class) into a variable in another area
# this tells us that printing Outside's n_to value will give us Foyer

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

# Make a new player object that is currently in the 'outside' room. ✅
name = input(
    "\n(͡° ͜ʖ ͡°)\nWelcome to my adventure game! \nI am a computer. What is your name?\n").lower().capitalize()
print(f"\n(͡° ͜ʖ ͡°)\nHi, {name.strip()}. It's a pleasure to meet you. Alright, I am going to make a new player for you to play as:\n\n\t\t(ง︡'-'︠)ง <= (that's you)\n\nWowwwww you look so cool!")

player = Player(name, room["outside"], [Item("Rubber Chicken", "Useless...")])

playing_prompt = input(
    "Ready to play? [Y]es or [N]o\n").lower()

if playing_prompt == "y":
    playing = True
    print("\n(͡° ͜ʖ ͡°)\nSweet! Let us begin... MWAHAHAHAHAHAH!")
elif playing_prompt == "n":
    playing = False
    print("\n(͡° ͜ʖ ͡°)\nOkay, maybe next time!")

while playing:
    # Prints the current room name
    print("\n\n", player.report_back())
    # Prints the current description (the textwrap module might be useful here).
    user_action = input(
        "Where would you like to go?\n[N]orth, [S]outh, [E]ast, [W]est, or [Q]uit\n").lower().split(" ")
    desired_items = []
    undesired_items = []

    # go where the user wants
    if user_action[0] == "q":
        # If the user enters "q", quit the game.
        print("Thanks for playing! See you next time.")
        playing = False
    elif user_action[0] == "n":
        # If the user enters a cardinal direction, attempt to move to the room there.
        # check if n_to is there
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
        else:
            print("This is a dead end. Try again.")
    elif user_action[0] == "s":
        # If the user enters a cardinal direction, attempt to move to the room there.
        # check if s_to is there
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
        else:
            print("This is a dead end. Try again.")
    elif user_action[0] == "e":
        # If the user enters a cardinal direction, attempt to move to the room there.
        # check if e_to is there
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
        else:
            print("This is a dead end. Try again.")
    elif user_action[0] == "w":
        # If the user enters a cardinal direction, attempt to move to the room there.
        # check if w_to is there
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
        else:
            print("This is a dead end. Try again.")
    # if the user wants to pick up an item
    elif user_action[0] == "get":
        desired_items.extend(user_action[1:])
        # add items to the player's inventory
        for desired_item in desired_items:
            if desired_item in items:
                player.pick_up(items[f"{desired_item}"])
            else:
                print(
                    f"\n\n\n(╥︣﹏᷅╥) ⚠ Oops! {desired_item.capitalize()} is not here.")
                # make direction invalid to give user another chance to pick up the item
    elif user_action[0] == "drop":
        # if a user wants to drop an item
        undesired_items.extend(user_action[1:])
        for undesired_item in undesired_items:
            player.drop(undesired_item)
    else:
        print("Please input an acceptable response to continue.")
