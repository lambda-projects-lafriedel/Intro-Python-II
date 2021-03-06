# Controller of MVC

from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "To the north, the cave mount beckons.", [Item("rock", "It's just a rock.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [Item("coins", "These will be useful in the market.")]),

    'overlook': Room("Grand Overlook", """A steep cliff reveals itself, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [Item("sword", "An emblem appears on the handle of this sword."), Item("key", "This key looks like it opens something important...")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", [Item("coins", "These will be useful in the market."), Item("medicine", "A corked vial filled with blue liquid."), Item("shield", "Made of heavy metal.")]),

    'treasure': Room("Treasure Chamber", """The long-lost treasure chamber has been found! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", [Item("map", "The map isn't for here, but could be useful later.")]),
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


# Main

# Make a new player object that is currently in the 'outside' room.
player = Player("Bob", room['outside'])

# Acceptable direction inputs
dirs = ["n", "e", "s", "w"]

# Function that decides if player can move
def player_advance(direction):
    if (direction == "n" and player.current_room == room['outside']) or \
        (direction == "n" and player.current_room == room['foyer']) or \
        (direction == "n" and player.current_room == room['narrow']):
        return 1
    elif (direction == "e" and player.current_room == room['foyer']):
        return 2
    elif  (direction == "s" and player.current_room == room['overlook']) or \
        (direction == "s" and player.current_room == room['foyer']) or \
        (direction == "s" and player.current_room == room['treasure']):
        return 3
    elif (direction == "w" and player.current_room == room['narrow']):
        return 4
    else:
        return 0

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
while True:
    print(f'\n{player.name} is currently in the {player.current_room.name}. {player.current_room.description}\n')
    
    player.current_room.room_inventory()

# * Waits for user input and decides what to do.
    choice = input(f'\nWhat direction shall {player.name} travel next? Choose a direction (n, e, s or w): ')
    print(f'\n{player.name} chose {choice}.\n')

    choice_list = choice.split()

#    If the user enters "q", quit the game.
    if len(choice_list) == 1:
        if choice_list[0] == "q":
            break

        elif (choice_list[0] == "i") or (choice_list[0] == "inventory"):
            player.player_inventory()

        elif choice_list[0] in dirs:
            move = player_advance(choice)
            if move == 0:
                print(f"{player.name} cannot move in that direction. Try again.\n")
            if move == 1:
                player.current_room = player.current_room.n_to
            if move == 2:
                player.current_room = player.current_room.e_to
            if move == 3:
                player.current_room = player.current_room.s_to
            if move == 4:
                player.current_room = player.current_room.w_to
        else:
            print("Invalid input.\n")
    # If len(choice) == 2, assume it's to perform an action on an item
    elif len(choice_list) == 2:
        
        input_item = choice_list[1]

        if (choice_list[0] == "get") or (choice_list[0] == "take"):

            if player.current_room.id_item(input_item):
                player.take_item(player.current_room.get_room_item(input_item))
                player.current_room.remove_item(input_item)
            else:
                print("That item does not exist in this room.")

        if (choice_list[0] == "drop"):
            if player.id_inventory(input_item):
                player.current_room.add_item(player.get_player_item(input_item))
                player.drop_item(player.get_player_item(input_item))
            else:
                print("That item does not exist in the inventory.")
    else:
        print("I don't understand that command.")


# Print an error message if the movement isn't allowed.