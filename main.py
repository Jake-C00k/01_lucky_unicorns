#Import all necessary
from random import randint


#Create Variables
yes = ["yes", "y", "yep", "affirmative"]
no = ["no", "n", "nope", "negative"]
low = 1
high = 10
instruction = False
min = 1
max = 100
round_start = False
start = True
first = True
fin = False

#Define functions
def instructions():
    input("Okay, Here are the instructions:")
    input(" -A token will be randomly generated by this program- ")
    input(" -It can be one of 4 types: Zebra, Horse, Donkey or Unicorn- ")
    input(" -If it is a Zebra or Donkey, you will win 50c,\n and if it is a Unicorn, you will win $5- ")
    input(" -Unfortunately, if it is a donkey, you will go home empty handed- ")

def yes_no(question):
    valid = False
    yes_no.play_again = True
    while not valid:
    # Ask question
        answer = input(question).lower().strip()
    # If yes, continue program
        if answer in list(yes):
            valid = True
            return answer
            return num_check.response

        elif answer in list(no) and fin == True:
            yes_no.play_again == False

        elif answer in list(no) and instruction == True:
            num_check("How many rounds do you want to play?\n ", low, high)

        elif answer in list(no) and round_start == True:
            yes_no.play_again == False
        elif answer in list(no):
            instructions()
            valid = True
        # If anything else
        else:
            print("Please answer with a yes or no answer")

def num_check(question, low, high):
    error = "Please give a whole number between {} and {} as your response\n".format(low, high)

    valid = False
    while not valid:
        try:
            #Ask question and get response
            if first == True:
                num_check.response = None
                num_check.response = int(input(question))

            else:
                num_check.response = int(input(question))
            #Check to see whether the response is expected
            if low <= num_check.response <= high:
                yes_no("Ok, so you want {} round/s?\n".format(num_check.response))
                return

            else:
                print(error)
        #If unexpected value, re-run question
        except ValueError:
            print(error)

def num_gen():
    for _ in range(1):
        value = int(randint(min, max))
        if 0 < value <= 25:
            num_gen.token = "Zebra"
            statement = "Not bad, could be worse\n"
            num_gen.value = 0.5
        elif 25 < value <= 50:
            num_gen.token = "Horse"
            statement = "Not bad, could be worse\n"
            num_gen.value = 0.5
        elif 50 < value <= 90:
            num_gen.token = "???????? Donkey ????????"
            statement = "Unlucky, hopefully you do better next time\n"
            num_gen.value = 0
        elif 90 < value <= 100:
            num_gen.token = "???????? Unicorn ????????"
            statement = "Wow, that's fantastic, you really won big!\n"
            num_gen.value = 5
    print("Generating token...")
    print("You got a {}".format(num_gen.token))
    print(statement)



#Main body
print("""
-----------------------------------
  ???? Welcome to Lucky Unicorns ????
-----------------------------------""")
yes_no("Have you played the lucky unicorn game before?\n ")
input("Okay then, we're ready to start!\n")
instruction = True
round_start = True
num_check("How much do you want to add to your balance ($1 = 1 round)\n ", low, high)
first = False
fin = True
while 0.5 < num_check.response and yes_no.play_again == True:
    num_gen()
    num_check.response -= 1
    num_check.response += num_gen.value
    print("Your current balance is: {}".format(num_check.response))
    yes_no("Continue playing?")

input("Thank you for playing the Lucky Unicorn game")
input("We hope you play again soon")
