def shape_name(question):
    error = "Please enter a shape with up to 4 sides"

    valid = False
    while not valid:

        # ask question and put response in lower case
        response = input(question).lower()

        if response == "triangle":
            return ""
        elif response == "square" or response == "rectangle":
            return "quad"
        elif response == "circle":
            return "circle"
        elif response == "trapezium":
            return "trapezium"
        else:
            print(error)


# main routine goes here

for item in range(0, 6):
    wanted_area = shape_name("What shape area do you want to find?")
    print("Answer OK, you said", wanted_area)
    print()
