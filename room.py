class Room():
    # create a room
    def __init__(self):
        self.name = None
        self.description = None
        self.linked_rooms = {}
        self.character = None

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def describe(self):
        print("You are in the " + self.name + ".")
        print("--------------------")
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is to the " + direction + ".")
        inhabitant = self.get_character()
        if inhabitant is not None:
            inhabitant.describe()
        return inhabitant

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self