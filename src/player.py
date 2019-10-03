# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'\nYour Current Player and Location:\n  Player =====> {self.name},\n  Location ===> {self.current_room}\n'

    def move(self,direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print(f"\n !!!!!!!!!There is no path in that direction! TRY AGAIN!!!!!!!!!!")
