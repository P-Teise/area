# functions go here


def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)


name = not_blank("Shape name: ", "Sorry - this can't be blank. Please enter a valid shape.")
