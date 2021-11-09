def shape_name(question):
    error = "Please enter a shape with up to 4 sides"

    valid = False
    while not valid:

        # ask question and put response in lower case
        response = input(question).lower()

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


# main routine goes here

wanted_area = shape_name("What shape area do you want to find?")
print("Answer OK, you said", wanted_area)
print()
