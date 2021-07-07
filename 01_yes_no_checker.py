# Ask the user if they have played before
played_before = input("Have you played this game before?").strip().lower()
# If yes, continue program
if played_before  == "yes" or played_before == "y":
    print("Lets begin")
# If no, display instructions
elif played_before == "no" or played_before == "n":
    print("Instructions")
# If anything else
else:
    print("Please answer with a yes or no answer")
