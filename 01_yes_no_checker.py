#Set up functions
def gamebeg():
    valid = False
    while not valid:
    # Ask the user if they have played before
        played_before = input("Have you played this game before?").lower().strip()
    # If yes, continue program
        if played_before  == "yes" or played_before == "y":
            valid = True
            print("Lets begin")
        # If no, display instructions
        elif played_before == "no" or played_before == "n":
            valid = True
            print("Instructions")
        # If anything else
        else:
            print("Please answer with a yes or no answer")


while "a" != "b":
    gamebeg()
