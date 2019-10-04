# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory =[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'PLAYER: {self.name}\nLOCATION: {self.current_room}'

    def move(self,direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(f"\nLOCATION: {self.current_room.name}\n"
                  f"DESCRIPTION: {self.current_room.description}\n"
                  f"NEAR BY ITEMS: {self.current_room.item}")
        else:
            print(f"\nYou just smacked a wall Genius!\n")

    def handleVerb(self, verb):
        verb = verb.split(" ")
        if verb[0] == "take":
            if verb[1] in self.current_room.item:
                self.current_room.item.remove(verb[1])
                self.inventory.append(verb[1])
                return print(f"You have picked up {verb[1]}")
            else:
                print("Invalid item take")
        elif verb[0] == "drop":
            if verb[1] not in self.current_room.item:
                self.inventory.remove(verb[1])
                self.current_room.item.append(verb[1])
                return print(f"You have dropped {verb[1]}")
            else:
                print("Invalid Item drop")





