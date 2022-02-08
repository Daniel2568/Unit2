'''
##################################
Lab 2.02 Booleans & Expressions
##################################
In your Notebook
Predict if each of the following examples will produce a True or False output. Check your answers in interactive mode.
                 
Example 1
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b == "science"       Prediction: false                    Actual: True
Example 2
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b != "science"       Prediction: false                    Actual:false
Example 3
    >>> a = 100
    >>> b = "science"
    >>> a > 75 or b != "science"        Prediction: false                    Actual: True
Example 4
    >>> a = 100
    >>> b = "science"
    >>> c = True
    >>> not c and a > 75 and b == "science"     Prediction: error             Actual: 'c' is not defined

In your Console

Complete the following coding challenge
Create a "Can I be President?" program, which determines if the user meets the minimum requirements for becoming the President of the United States. 
Have the user input the information needed.

The minimum requirements to be president of the United States are:

1. Older than 35

2. Resident of US for 14 Years

3. Natural born citizen

Print True if the person could be president and False if they can't be president.

Create a "I can't be President?" program. Print True if the user cannot be President and False if they can be President.

Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. Because of a legal loophole, if you are over the age of 18 you can ride regardless of your height. If you are allowed to ride, the coaster costs 4 quarters (although the operator accepts tips so more money is appreciated).

Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. Print True if the person can ride and False if they can't.


Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same
not(x or y) == not x and not y

not(x and y) == not x or not y
'''
print('Can you be president? Lets see if you qualify! ')
required_age = '35'
required_resident = '14'
born_in_US = 'yes'
user_age = input('How old are you?> ')
user_resident = input ('How many years have you been a US resident?>')
user_born = input ('Are you born in the US? [yes or no]   ')
can_you_be_president = (user_age >= required_age) and (user_resident >= required_resident) and (user_born == born_in_US)
print(can_you_be_president) 
'''
#I Can't be president?

'''
print('I cant be president? ')
required_age = '35'
required_resident = '14'
born_in_US = 'yes'
user_age = input('How old are you?>')
user_resident = input ('How many years have you been a US resident?>')
user_born = input ('Were you born in the US? [yes or no]   ')
can_you_be_president = (user_age >= required_age) and (user_age >= required_age) and (born_in_US == user_born)
print(can_you_be_president)


#Can i Ride the roller coaster?

print('can you ride the roller coaster? well lets find out!')
required_height = '50'
minimum_age_for_no_height_requirement = '18'
minimum_quarters_to_go_on_ride = '4'
frequent_rider_pass = 'yes'
user_height = input (' How tall are you in inches?> ')
user_age_for_roller_coaster = input ('How old are you?> ')
user_quarters = input ('How many quarters do you have on you to pay for this roller coaster?> ')
user_pass = input('do you have a frequent rider pass? [yes or no] ')
can_you_go_on_the_roller_coaster = (user_height >= required_height) and (user_quarters >= minimum_quarters_to_go_on_ride) or (user_age_for_roller_coaster >= minimum_age_for_no_height_requirement) and (user_pass == frequent_rider_pass)
print (can_you_go_on_the_roller_coaster)