#Define variables
low = 1
high = 10
def num_check(question, low, high):
    error = "Please enter a whole number between {} and {}\n".format(low, high)

    valid = False
    while not valid:
        try:
            #Ask question and get response
            response = int(input(question))

            #Check to see whether the response is expected
            if low <= response <= high:
                return response

            else:
                print(error)
        #If unexpected value, re-run question
        except ValueError:
            print(error)

#while "a" != "b":
    #num_check("Please enter a number between {} and {} ".format(low, high), low, high)

