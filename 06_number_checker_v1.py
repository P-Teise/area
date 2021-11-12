# functions go here

def int_check(question, low_num, high_num):

    error = "Please enter a valid number higher than {}". format(low_num)

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if low_num <= response:
                return response
            if response = str(input())
            else:
                print(error)

        # if integer is not entered, display an error message
        except ValueError:
            print(error)

# main routine goes here


length = int_check("Length 1: ", 0, 130)
