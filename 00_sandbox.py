#Set up Variables
get_age = None

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
