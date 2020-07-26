import time

class Character():
    # create character
    def __init__(self):
        self.name = None
        self.description = None
        self.conversation = None
        self.location = None
        self.item = None

    def set_name(self, char_name):
        self.name = char_name

    def get_name(self):
        return self.name

    def set_description(self, char_description):
        self.description = char_description

    def get_description(self):
        return self.description

    def set_location(self, room_name):
        self.location = room_name

    def get_location(self):
        return self.location

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    # describe character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # talk to character
    def talk(self, carrying):
        print("")
        time.sleep(1)
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you...")
        if self.item is not None:
            print(self.name + " is carrying a " + self.item.name + ".")
        return carrying

    # fight character
    def fight(self, carrying, current_room):
        print("")
        time.sleep(1)
        print("What will you fight with? >")
        combat_item = input()
        try:
            if combat_item == carrying.name:
                print("[" + self.name + " says]: Stop waving that " + carrying.name + " about.")
                print(self.name + " is very upset and doesn't want to fight you.")
            else:
                print("You don't have a " + combat_item + ".")
                print("You are carrying a " + carrying.name + ".")
        except:
            print("You don't have a " + combat_item + ".")
        return True, carrying

    # give something to the character
    def gift_something(self, carrying, current_room):
        print("What are you carrying as a gift for me?")
        print("")
        time.sleep(1)
        try:
            print("Thank you for your kind offer but I cannot accept this " + carrying.name)
        except:
            print("You're trying to be kind but you aren't carrying anthing.")
        return True, carrying

    def escape(self):
        print("Well done - you have won the game!")
        donnie = "yes"
        return False, donnie

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.weakness = None

    def set_weakness(self, item):
        self.weakness = item

    def get_weakness(self):
        return self.item

    def fight(self, carrying, current_room):
        print("")
        time.sleep(1)
        print("What will you fight with? >")
        print("")
        time.sleep(1)
        combat_item = input()
        try:
            if combat_item == carrying.name:
                if combat_item == self.weakness.name:
                    print("You fend " + self.name + " off with the " + combat_item)
                    carrying = self.item
                    current_room.set_character(None)
                    return True, carrying
                else:
                    print("[" + self.name + " says]: Why are you waving that " + carrying.name + " you fool, ha ha - you die!")
                    print("")
                    time.sleep(1)
                    print("GAME OVER")
                    return False, carrying
            else:
                print("You don't have a " + combat_item + ".")
                print("You are carrying a " + carrying.name + ".")
                return True, carrying
        except:
            print("You don't have a " + combat_item + ".")
            print("")
            time.sleep(1)
            print("GAME OVER")
            return False, carrying

    def gift_something(self, carrying, current_room):
        print("What, are you offering me gift  - you foolish fool?")
        print("")
        time.sleep(1)
        try:
            print("Thank you, but I find I must kill you with this " + carrying.name)
        except:
            print("Is this supposed to be an insult? You aren't carrying anthing - ha ha - I kill you!")
        return False, carrying

class Friend(Character):
    def __init__(self):
        super().__init__()

    def talk(self, carrying):
        print("")
        time.sleep(1)
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you...")
        if self.item is not None:
            print(self.name + " is carrying a " + self.item.name + ".")
            print("")
            time.sleep(1)
            print("[" + self.name + " says]: I have a gift for you... " + self.name + " offers you a " + self.item.name + "...")
            print("but remember..., you can only carry one item at a time.")
            accept_gift = input("Do want to accept the "+ self.item.name + "? [yes, no]>")
            print("")
            time.sleep(1)
            if accept_gift == "yes":
                print(self.name + " gives you a " + self.item.name + ".")
                carrying = self.item
                self.item = None
            else:
                print("Well, come back if you change your mind...")
                carrying = carrying
        return carrying

    def gift_something(self, carrying, current_room):
        try:
            print("What are you carrying as a gift for me?")
            print("")
            time.sleep(1)
            if self.name == "ted":
                if carrying.name == "shield":
                    carrying = None
                    print("""A shield - thank you - wait... wow, I can see my
beautiful face - you can leave the caslte now with my blessing!""")
                    print("")
                    time.sleep(1)
                    current_room.get_details()
                    print("Well done - you have won the game!")
                else:
                    print(self.name + "has run away!")
                    print("")
                    time.sleep(1)
                    print("GAME OVER")
                return False
            else:
                print("Thank you for your kind offer but I cannot accept this " + carrying.name + ".")
        except:
            print("You're trying to be kind but you aren't carrying anthing.")
        return True, carrying