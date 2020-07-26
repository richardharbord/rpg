class RPGInfo():
    author = "Anonymous"

    @classmethod
    def set_author(cls, author):
        cls.author = author

    @classmethod
    def get_author(cls):
        return cls.author

    def __init__(self):
        self.title = "game"

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def welcome(self):
        print("Welcome to " + self.title + "!")
        print("""Find your way through the maze of rooms - meeting strange characters along
the way! You can 'talk' to, and 'fight' the characters you meet - each has a different item
that you can get if you fight them. But beware..., not all items are good for fighting. Find
out everything you can from the characters and solve the puzzle...""")
        print("")

    def instructions(self):
        print("To go north, south, east or west - type: north, south, east or west.")
        print("To talk, fight, or give away (gift) what you are carrying - type: talk, fight or gift.")
        print("To see the instructions again - type: instructions.")
        print("You can only carry one item at a time")

    @staticmethod
    def info():
        print("Made using the OOP RPG creator (c) me :-)")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)