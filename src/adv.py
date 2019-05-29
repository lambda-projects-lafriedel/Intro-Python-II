from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "To the north, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff reveals itself, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """The long-lost treasure
chamber has been found! Sadly, it has already been completely emptied by
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
    print(f'{player.name} is currently in the {player.current_room.name}. {player.current_room.description}\n')

# * Waits for user input and decides what to do.
    choice = input(f'What direction shall {player.name} travel next? Choose a direction (n, e, s or w): ')
    print(f'\n{player.name} chose {choice}.\n')

# If the user enters "q", quit the game.
    if choice == "q":
        break
# If the user enters a cardinal direction, attempt to move to the room there.
    elif choice in dirs:
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
# Print an error message if the movement isn't allowed.


