#Import random number generator
from random import randint

#Set up Variables
get_age = None
prize = "🎁"
no_prize = "😔"
#Check to see whether the age is a valid number
while get_age == None:
    try:
        get_age = int(input("Please enter your age as an integer."))
        while get_age <= 0 or get_age >= 123:
            get_age = int(input("Sorry, {} isn't currently a possible age, please enter a number.".format(get_age)))
    except ValueError:
        print("That isn't an integer.")

#Show the user their age
print("You are {} years old".format(get_age))

input("We will now generate a number, if your age is higher than this number, you will win a prize!")

#Store a minimum and maximum value for the random generator
min = get_age - 5
max = get_age + 20

#generate a random number
for _ in range(1):
	value = randint(min, max)
	print("The number is... {}".format(value))

#Check whether the number is greater
if value < get_age:
    print("Hooray, you won!")
    print(prize)
else:
    print("Sorry, today isn't your lucky day.")
    print(no_prize)
