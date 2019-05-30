# Model level of MVC -- database level. think of Room class as a db table, and attributes are columns. The x_tos are like FK that point to other rooms

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None

    # Prints the room's inventory
    def room_inventory(self):
        if len(self.items) == 0:
            print("There are no items in this room.")
        else:
            print("Items in this room:")
            for item in self.items:
                print(item)
    
    # Checks if player's requested item is in the room
    def id_item(self, requested_item):
        for item in self.items:
            if item.name == requested_item:
                return True
        return False

    # Removes an item from the room
    def remove_item(self, requested_item):
        for item in self.items:
            if item.name == requested_item:
                self.items.remove(item)
    
    # Adds an item to the room
    def add_item(self, dropped_item):
        self.items.append(dropped_item)
    
'''
    Could use a __str__ here to print name and description without using print()
'''
