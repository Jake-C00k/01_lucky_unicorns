#Import random number generator
from random import randint

#Set up Variables
get_age = 0
prize = "🎁"
no_prize = "😔"
streak = 0
high_score = 0
value =  0
round =  1

def gen():
    for _ in range(1):
        value = int(randint(min, max))
        print("The number is... {}".format(value))
        return value

def gensecret():
       for _ in range(1):
        value = int(randint(sec_min, sec_max))
        print("The number is...{}".format(value))

def instructions():
    input("We will ask your age and then generate a number, if your age is higher than this number, you will win a prize! ")

played_before = ("")
#Checks if user has played before
while played_before.lower().strip() != "yes":
    played_before = str(input("Have you played the age game before? ")).lower().strip()
    if played_before == "no" or played_before == "n":
        instructions()
        break
    if played_before == "yes" or played_before == "y":
     break
    else:
        print("Sorry, there was an error, please re-enter and make sure your answer is a yes or no.")
        played_before = ("")

secret = input("Lets begin. ").lower().strip()

#Check to see whether the age is a valid number
while get_age == 0:
    try:
        get_age = int(input("Please enter your age as an integer."))
        while get_age <= 0 or get_age >= 123:
            get_age = int(input("Sorry, {} isn't currently a possible age, please enter a number.".format(get_age)))
    except ValueError:
        print("That isn't an integer.")

#Show the user their age
print("You are {} years old".format(get_age))

#Store a minimum and maximum value for the random generator
min = get_age - 5
max = get_age + 20

sec_min = get_age - 20
sec_max = get_age + 5

#generate a random number
if secret == "u u d d l r l r b a s":
    print("Cheat code activated: Konami code ")
    gensecret()
else:
    gen()
#Check whether the number is greater
if value < get_age:
    print("Hooray, you won! ")
    input(prize)
    win = "yes"
    streak += 1
else:
    print("Sorry, today isn't your lucky day. ")
    input(no_prize)
    win = "no"
#Asks user if they would like to continue
if win == "yes":
    play_again = input("Would you like to continue playing? ")
    round += 1
else:
    print("Thanks for playing the game, try again soon. ")

if play_again == "yes" or play_again == "sure":
    print("Round {}: ".format(round))
    round = 1
