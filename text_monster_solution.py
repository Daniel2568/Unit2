# Text Monster Game 

# Map of dungeon 
dungeon = [
    ['prize', 'boss monster','sword','stairs down'], #floor 0
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
        print("You are in an empty room") #make this more intresting 
    elif location == 'sword' :
        print("You see a sword") #make this more intresting 
    elif location == 'stairs up' :
        print("You see some stairs leading down") #make this more intresting 
    elif location == 'monster' :
        print("You see a scary monster") #make this more intresting
    
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

