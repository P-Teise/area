# Functions go here
# notify user first

instruction: str = "Hi! You can calculate the area of shapes with up to 4 sides"
print(instruction)


# check that shape name is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question).lower()

        if response != "":
            return response
        else:
            print(error_message)


# shape name checker
def shape_name():
    error = "Please enter a shape with up to 4 sides"

    valid = False
    while not valid:

        # ask question and put response in lower case
        response = input().lower()

        if response == "triangle":
            return "triangle"
        elif response == "square":
            return "square"
        elif response == "rectangle":
            return "rectangle"
        elif response == "rhombus":
            return "rhombus"
        elif response == "kite":
            return "kite"
        elif response == "circle":
            return "circle"
        elif response == "trapezium":
            return "trapezium"
        else:
            print(error)

    # notify user of units
    units_instruction: str = "Please enter the lengths of your desired shape in metres"
    print(units_instruction)


# checks for an integer more than 0


# ******* Main routine ***********

# <<<<<<< Loop to get shape detail >>>>>>>>
# start of loop
# initialise loop so that it runs at least once


# Get name (can't be blank)
name = not_blank("Shape name: ", "Sorry - this can't be blank. Please enter a valid shape.")

# Get valid shape (has to be in boundary)

wanted_area = shape_name()
print("Answer OK, you said", )
print()

# End of shape loop
