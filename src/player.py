# Model level of MVC -- database level. think of Player class as a db table

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    # Add item to player's inventory
    def take_item(self, item):
        self.inventory.append(item)
        item.on_take()
    
    # Remove item from player's inventory
    def drop_item(self, item_to_drop):
        for item in self.inventory:
            if item.name == item_to_drop:
                self.inventory.remove(item)
                item.on_drop()
    
    # Prints list of player's current inventory
    def player_inventory(self):
        if len(self.inventory) == 0:
            print("No items being carried.")
        else:
            print("Carrying:")
            for item in self.inventory:
                print(item)

    # Checks if item to drop is in player's inventory
    def id_inventory(self, requested_item):
        for item in self.inventory:
            if item.name == requested_item:
                return True
        return False

    # Gets whole item tuple to be transferred
    def get_player_item(self, dropped_item_name):
        for item in self.inventory:
                if item.name == dropped_item_name:
                    return item
