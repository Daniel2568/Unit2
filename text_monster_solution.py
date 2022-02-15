# Text Monster Game 

# Map of dungeon 
from calendar import c


dungeon = [
    ['prize', 'boss monster','sword', 'emtpy', 'stairs down'], #floor 0
    ['magic stones', 'monster','stairs down', 'empty', 'stairs up'], #floor 1
    ['empty', 'sword','stairs up', 'monster', 'empty'] #floor 2
    ]

# Player info 
Inventory = []
current_room = 0
current_floor = 2
location = dungeon[current_floor][current_room]

#game loop
while True:

    # update location 
    location = dungeon[current_floor][current_room]


    # describe where we are to the user 
    if location == 'empty' :
        print("You are in an empty room. The walls seem to be a bit mossy and gross with... who knows")  
    elif location == 'sword' :
        print("You see a sword in the middle of the room. It looks pretty shiny and seems to have a faint glow. It is very tempting to go and try to grab it.")
    elif location == 'stairs up' :
        print("You see some stairs that seem to be going up") 
    elif location == 'monster' :
        print("You see a weird thing that has goo all over it and seems to be picking it's nose") 
    elif location == 'stairs down' : 
        print("You see some stairs going down") 
    elif location == 'magic stones' :
        print("You found a room with some glowing weird stones. Maybe thats what the crazy wizard was asking you to get") 
    elif location == 'boss monster' :
        print("You found an abnormally big and disformed thing that is very muscular and 10ft tall. It doesn't look very happy, good luck") 
    else: 
        print("You have found some gold, potions, and a sheild with a sword enscribed with an enchanment saying the sword never breaks")
    
    #player choices 
    player_choices = input("What would you like to do?[move left, right, up, down, grab, fight]")
    print(player_choices)

    if player_choices == 'right' :
        current_room += 1 
        if current_room == 5: 
            print("You can't move in that direction, you are running into the wall")
            current_room = 4
    elif player_choices == 'left' :
        current_room -= 1
        if current_room == -1:
            print("You can't move in that direction, you are running into the wall")
            current_room = 0 
    elif player_choices == 'up' :
        if location == 'stairs up' :
            current_floor -= 1 
        else:
            print("You cannot move up or down anymore. The stairs only go down or there are no stairs to go up or down")
    elif player_choices == 'down' :
        if location == 'stairs down' :
            current_floor += 1
        else: 
            print("You cannot move up or down anymore. The stairs only go down or there are no stairs to go up or down") 
    elif player_choices == 'grab' :
        if location == 'sword' : 
            Inventory.append(location)
            dungeon[current_floor][current_room] = 'empty'
        elif location == 'magic stones':
            Inventory.append(location)
            dungeon[current_floor][current_room] = 'empty'
        elif location == 'monster' or location == 'boss monster': 
            print("what a nice choice") #make this more intresting
    elif player_choices == 'inventory' : 
        print("You have:") # if you want to test a(the) program without getting errors then type "pass" under the code with no quotes
        print(' '. join(Inventory)) # and it will ignore the code "pass" is under
    

    elif player_choices == 'fight' :
        pass
        #hjkdshjkhskjhkj 
        if location == 'monster' :
            pass 



