'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''


#
#
#
#
#
#

print('I will be predicting when you will turn 100.')
user_name = input ('What is your name?> ')
user_age = int(input ('How old are you?> '))
birth_year = 2022 - user_age
when_user_turns_100 = 100 + birth_year
print(user_name + " You will turn 100 in the year ")
print (when_user_turns_100)