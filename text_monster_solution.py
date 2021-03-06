# Text Monster Game 

print("Welcome to Text Monster Adventure!")
print("You live in a small town in the mythical world of magic. One day you wake up and check your mail")
print("Player: Oh, whats this? A letter from the Grand Wizard Gandolf.")
print("You open the letter. The letter says:\nDear Player,\nI am in need of some help that may require some explanation.\nCome as soon as you can.\nfrom, Gandolf-")
print("You get ready and go to his house")
print("You knock on the door")
print("Gandolf answers: Ahh I see you have found my letter. Come in I have things to tell you\nyou walk into the house and go into the dining room")
print("Gandolf: I have a problem, You see I have some stone that have gotten stolen from me.\nNow I know who stole them but the problem is getting them back\nI am getting very old and need you to get them for me.\nIt is a lot to ask but if you're up for the task you will be rewarded handsomely")
print("You think about the quest you are given.\nGandolf: Oh and before you make a final decision the quest will take place in the dungeon of Garabond,\nthere you will find the stones somewhere in the dungeon, there will also be monsters you need to fight\nAll the equipment you will need, you should be able to find in the dungeon\nGoodluck")
print("You take this into consideration and say: Alright Gandolf, where do I go")
print("Gandolf gives you a map and tells you where to go")
print("You make it to the dungeon and find the entrence")
print("You open the door and find that it is very dark at first, your eyes start to adjust and you start to see everything")
print("----------------------------------------------")

# Map of dungeon 



dungeon = [
    ['prize', 'boss monster','sword', 'emtpy', 'stairs down'], #floor 0
    ['magic stones', 'monster','stairs down', 'empty', 'stairs up'], #floor 1
    ['empty', 'sword','stairs up', 'monster', 'empty'] #floor 2
    ]

# Player info 
Game_Over = False 
dead = False 
inventory = []
current_room = 0
current_floor = 2
location = dungeon[current_floor][current_room]

#game loop

while Game_Over == False:

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
        print("You see a weird thing that has goo all over it and seems to be picking it's nose\nYou better get out of there quick before he hits gold and sees you") 
    elif location == 'stairs down' : 
        print("You see some stairs going down") 
    elif location == 'magic stones' :
        print("You found a room with some glowing weird stones. Maybe thats what the crazy wizard was asking you to get") 
    elif location == 'boss monster' :
        print("You found an abnormally big and disformed thing that is very muscular and 10ft tall. It doesn't look very happy, good luck") 
    else: 
        print("You have found some gold, potions, and a sheild with a sword enscribed with an enchanment saying the sword never breaks\nYou might not be able to grab these but you will automatically grab them once the game is over")
    
    #player choices 
    player_choices = input("What would you like to do?[move left, right, up, down, grab, fight, inventory]")
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
            inventory.append(location)
            dungeon[current_floor][current_room] = 'empty'
        elif location == 'magic stones':
            inventory.append(location)
            dungeon[current_floor][current_room] = 'empty'
        elif location == 'monster' or location == 'boss monster': 
            print("That probably wasn't the smartest choice ever and now the monster is not only confused but now extremely furious") 
    elif player_choices == 'inventory' : 
        print("You have:") # if you want to test a(the) program without getting errors then type "pass" under the code with no quotes
        print(' '. join(inventory)) # and it will ignore the code "pass" is under
    

    elif player_choices == 'fight' :

        if location == 'monster' :
            if 'sword' in inventory:
                print("You have made your choice to attempt to kill this little annoying gross hairy thing.") 
                print(f"You found it was easier than you thought it would be to try and destroy this hairy mop \nThe only problem is that your sword broke")
                inventory.remove('sword')
                dungeon[current_floor][current_room] = 'empty'
                print(f"the current location is {dungeon[current_floor][current_room]}")
                 
            else: 
                print(f"That wasn't very smart now wasn't you dummy\nYou Died and the moster still remains") #make this more intresting
                dead = True  
        if location == 'boss monster' :
            if 'sword' and 'magic stones' in inventory:
                print("You will try to kill the boss monster") # make this more intresting 
                dungeon[current_floor][current_room] = 'empty'
                print(f"the current location is {dungeon[current_floor][current_room]}")
                print("You have vanquished the boss monster you may now move on without worry")
                
                Game_Over = True 
            else: 
                print("That wasn't very smart now wasn't you dummy.\nYou Died and the moster still remains, if you haven't already go grab the magic stones to defeat the boss monster") #make this more intresting
                dead = True 
                Game_Over = True

# determine win/loss
    if Game_Over == True:
        if dead == True: 
            print("Game Over")
            print("You died trying to fight a monster with your fingers")
        else: 
                print("You won!")
                print("You helped the wizard with his problems. He is very thankful and has given you some neat potions and gifts.")

        # play again?
        user_input = input("Would you like to play again? (y/n)")
        if user_input == 'y':
            # Player info 
            Game_Over = False 
            dead = False 
            inventory = []
            current_room = 0
            current_floor = 2
            location = dungeon[current_floor][current_room]
            dungeon = [
        ['prize', 'boss monster','sword', 'emtpy', 'stairs down'], #floor 0
        ['magic stones', 'monster','stairs down', 'empty', 'stairs up'], #floor 1
        ['empty', 'sword','stairs up', 'monster', 'empty'] #floor 2
        ]
        
        else:
            print("Thanks for playing, Have a great day")



