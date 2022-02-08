'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction:
Actual:

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction:
Actual:

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

# get three sides of a triangle
# use print statements/functions to make sure things are working
x = int(input("What is x?"))
y = int(input("What is y?"))
z = int(input("What is z?"))


#can it be a triangle 
if x + y > z and x + z > y and y + z > x:
    print(f"Perimeter of the triangle is: {x + y + z}")
    
    
    #is it a right triangle 
    if x ** z + y ** 2 == z ** 2:
        print("This is a right triangle.")

        #is determine if its an iscosolese, scalene, or equalateral
    if x == y and y == z:
        print("This is an equalateral triangle.")
    elif x == y or z == y or x == z:
        print("This ia an iscosoles triangle.")
    else:
        print("This is scalene triangle.")
else: 
    print("This is not a triangle.")

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''

#prizes 


prize_1 = 'Apple_Watch_SE'
prize_2 = 'Mystery_Box'
prize_3 = 'Airpods'
prize_4 = 'hat'
prize_5 = '$10,000'
prize_6 = 'Jar_of_pickles'
prize_7 = 'Winning_lotery_ticket'
prize_8 = 'Bucket_of_sardines'
prize_9 = 'Pie_face_slap'
prize_10 = 'Any_Phone_of_Choice'

#user chooses the prize door

user_chooses_the_door_with_a_prize_behind_it = input("Which door would you like to pick [pick doors from 1-10]?>")

#user gets any of the given prizes 

if user_chooses_the_door_with_a_prize_behind_it == '1': 
    print(prize_1)
    if user_chooses_the_door_with_a_prize_behind_it == '2':
        print(prize_2)
    if user_chooses_the_door_with_a_prize_behind_it == '3':
        print(prize_3)
    if user_chooses_the_door_with_a_prize_behind_it == '4':
        print(prize_4)
    if user_chooses_the_door_with_a_prize_behind_it == '5':
        print(prize_5)
    if user_chooses_the_door_with_a_prize_behind_it == '6':
        print(prize_6)
    if user_chooses_the_door_with_a_prize_behind_it == '7':
        print(prize_7)
    if user_chooses_the_door_with_a_prize_behind_it == '8':
        print(prize_8)
    elif user_chooses_the_door_with_a_prize_behind_it == '9':
        print(prize_9)
    else:
        print(prize_10)




