# functions go here

def units(question):
    error = "Enter valid units for length"

    valid = False
    while not valid:

        # ask question and put response in lower case
        response = input(question).lower()

        if response == "mm" or response == "millimetres":
            return "mm"
        elif response == "cm" or response == "centimetres":
            return "cm"
        elif response == "m" or response == "metres":
            return "m"
        elif response == "in" or response == "inches":
            return "in"
        elif response == "km" or response == "kilometres":
            return "km"
        else:
            print(error)


# main routine goes here

wanted_area = ("What shape area do you want to find?")
print("Answer OK, you said", wanted_area)
print()
