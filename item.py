class Item():
    # create an item
    def __init__(self):
        self.name = None
        self.description = None
        self.character = None

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def set_location(self, room_name):
        self.location = room_name

    def get_location(self):
        return self.location

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character