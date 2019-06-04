class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'

    # Prints confirmation that item was taken
    def on_take(self):
        print(f'Picked up {self.name}')

    # Prints confirmation that item was dropped
    def on_drop(self):
        print(f'Dropped {self.name}')