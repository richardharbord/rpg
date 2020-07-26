import room
import item
import character
import rpginfo
import time

spooky_castle = rpginfo.RPGInfo()
spooky_castle.set_title("The Spooky Castle")

# rooms
stairs = room.Room()
stairs.set_name("Winding Staircase")
stairs.set_description("An ancient banistered winding staircase  - broken in places.")

landing = room.Room()
landing.set_name("Broken Landing")
landing.set_description("A broken and creaking landing - you don't feel safe up here - but there is something familiar...")

kitchen = room.Room()
kitchen.set_name("Kitchen")
kitchen.set_description("A dank and dirty room, buzzing with flies.")

cupboard = room.Room()
cupboard.set_name("Kitchen Cupboard")
cupboard.set_description("A dark recess behind a creaky door - it's very dark.")

ballroom = room.Room()
ballroom.set_name("Ballroom")
ballroom.set_description("A vast room with a dark wooden floor: huge candlesticks guard the entrance.")

dining_hall = room.Room()
dining_hall.set_name("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

hall = room.Room()
hall.set_name("Hall")
hall.set_description("A long hall - full of spiders' webs - at the far end of the hall, there is a staircase.")

bedroom = room.Room()
bedroom.set_name("Master Bedchamber")
bedroom.set_description("A sickly smelling room with a curtained four poster at the centre - you can hear breathing...")

# room links
hall.link_room(kitchen, "east")
hall.link_room(dining_hall, "south")
hall.link_room(stairs, "north")
kitchen.link_room(dining_hall, "south")
kitchen.link_room(cupboard, "east")
kitchen.link_room(hall, "west")
cupboard.link_room(kitchen, "west")
stairs.link_room(hall, "south")
stairs.link_room(landing, "west")
landing.link_room(stairs, "east")
landing.link_room(bedroom, "west")
bedroom.link_room(landing, "east")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(hall, "north")
dining_hall.link_room(ballroom, "south")
ballroom.link_room(dining_hall, "north")

# items
sword = item.Item()
sword.set_name("sword")
sword.set_description("A normal fighting blade.")

wand = item.Item()
wand.set_name("wand")
wand.set_description("A small wooden stick.")

shield = item.Item()
shield.set_name("shield")
shield.set_description("A very shiny bronze shield.")

yo_yo = item.Item()
yo_yo.set_name("yo-yo")
yo_yo.set_description("A wheel on a string - keeps going up and down.")

# characters
spider = character.Character()
spider.set_name("A Spider")
spider.set_description("Quite a big black shiny spider - its legs are spinning webbing.")
spider.set_location(cupboard)
cupboard.set_character(spider)

don = character.Friend()
don.set_name("Don")
don.set_description("He is hiding in the four poster and wont come out.")
don.set_conversation("""This was not a good plan was it - I think we made a mistake,
what were we thinking - coming into this nightmare?""")
don.set_item(yo_yo)
don.set_location(bedroom)
bedroom.set_character(don)

bob = character.Enemy()
bob.set_name("Bob")
bob.set_description("A very sick man.")
bob.set_conversation("I smell really bad!")
bob.set_weakness(sword)
bob.set_item(shield)
bob.set_location(dining_hall)
dining_hall.set_character(bob)
wand.set_character(bob)

sam = character.Enemy()
sam.set_name("Sam")
sam.set_description("A frightening ghostly figure.")
sam.set_conversation("What - you can see me?")
sam.set_weakness(wand)
sam.set_item(sword)
sam.set_location(kitchen)
kitchen.set_character(sam)
sword.set_character(sam)

ted = character.Friend()
ted.set_name("Ted")
ted.set_description("A small, shabby brown rabbit that is staring at you.")
ted.set_conversation("""Although I have never seen myself - I know myself! I know
the in's and the out's of the up's and the down's! The wand is the way
to save the day from freaky things from far away. Don't use things sharp
on things that moan or else you wont be going home. Magic kills magic and
steel kills men... don't get the clue - then ask again...""")
ted.set_item(wand)
ted.set_location(ballroom)
ballroom.set_character(ted)
yo_yo.set_character(ted)

# start game
spooky_castle.welcome()
rpginfo.RPGInfo.info()
spooky_castle.instructions()
current_room = hall
carrying = None
donnie = "no"

game_state = True
while game_state == True:
    print("")
    time.sleep(1)
    inhabitant = current_room.get_details()
    if carrying is not None:
        print("You are carrying a " + carrying.name + ".")
        print(carrying.get_description())
    else:
        print("You are carrying nothing.")
    print("--------------------")
    command = input("> ")

    # response options
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            carrying = inhabitant.talk(carrying)
        else:
            print("Talking to yourself again... aye?")
    elif command == "fight":
        if inhabitant is not None:
            game_state, carrying = inhabitant.fight(carrying, current_room)
        else:
            print("Ha ha... fighting shadows?")
    elif command == "gift":
        game_state, carrying = inhabitant.gift_something(carrying, current_room)
    elif command == "instructions":
        spooky_castle.instructions()

    elif command == "Don":
        if current_room == bedroom:
            print("OK - I'll come with you... even though I hate you!")
            game_state, donnie = inhabitant.escape()
        else:
            print("Speak Engish!")
            spooky_castle.instructions()
    else:
        print("Speak Engish!")
        spooky_castle.instructions()

if donnie == "yes":
    print("You saved Don")
else:
    print("You didn't save Don so you haven't won the game sorry....")

rpginfo.RPGInfo.set_author("Richard")
rpginfo.RPGInfo.credits()