# Model level of MVC -- database level. think of Player class as a db table

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def take_item(self, item):
        self.inventory.append(item)
    
    def drop_item(self, item):
        self.inventory.remove(item)
    
    def player_inventory(self):
        if len(self.inventory) == 0:
            print("No items being carried.")
        else:
            print("Carrying:")
            for item in self.inventory:
                print(item)
