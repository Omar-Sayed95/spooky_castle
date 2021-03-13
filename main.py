from room import Room
from character import Enemy, Friend
from rpginfo import RPGInfo
from item import Item

spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()
RPGInfo.author = "Stemate"

#Add room objects here

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

#Add code to link between rooms here

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
#Set room character here

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there.")
#Set room character here

cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
#Set room item here

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
#Set room item here

#Set the current room here
backpack = []

dead = False
while dead == False:
    print("\n")         
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    
    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
       
    elif command == "fight":
        # You can check whether an object is an instance of a particular
        # class with isinstance() - useful! This code means
        # "If the character is an Enemy"
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")        

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)

RPGInfo.credits()
