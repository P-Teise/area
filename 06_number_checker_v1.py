# functions go here

def int_check(question, low_num):

    error = "Please enter a valid number higher than {}".format(low_num)

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            value_1 = float(input(question))

            if value_1 > low_num:
                return value_1

            else:
                print(error)

        # if integer is not entered, display an error message
        except ValueError:
            print(error)


# main routine goes here

length = int_check("Enter Length 1: ", 0)
print("Answer, OK you said:", length)
print()

