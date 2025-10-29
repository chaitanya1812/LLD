class Room:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"This is the {self.name}")


class House:
    def __init__(self, rooms):
        self.rooms = []
        for r in rooms: self.rooms.append(Room(r)) # Room object is managed by house object

    def show_house_layout(self):
        for room in self.rooms:
            room.describe()