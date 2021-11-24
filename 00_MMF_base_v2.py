# define list of shapes to make identifying what shape is valid easier
shapes_list = ['square', 'circle', 'trapezium', 'triangle', 'rhombus', 'kite']

units_short = ['mm', 'cm', 'm', 'km', 'ft', 'in']
units_long = ['millimetre', 'centimetre', 'metre', 'kilometre', 'feet', 'inches']


# start shape select function
def shape_select(q):
    # define name as input to question
    name = input(q).lower()

    # test if shape name is blank
    if not name:
        print('Error! please enter a shape')
        return 'err'

    # begin loop of shape identification
    a = 0
    while a < len(shapes_list):
        # if shape is valid return name of the shape
        if shapes_list[a] == name:
            return name
        # if shape is not found through one iteration of the loop, continue to the next
        elif shapes_list[a] != name:
            a += 1
            # if a has reached the same length as the length of the shapes list then print error and return err
            if a == len(shapes_list):
                print('Error! please select an appropriate shape')
                return 'err'


# identify which units the user is using
def units_select(q):
    reply = input(q).lower()

    b = 0
    while b < len(units_long):
        if reply[0] == 'c':
            return 'cm'
        elif reply[0] == 'k':
            return 'km'
        elif reply[0] == 'f':
            return 'feet'
        elif reply[0] == 'i':
            return 'inch'
        elif reply[0] == 'm':
            if reply[1] == 'i':
                return 'mm'
            elif reply[1] == 'm':
                return 'mm'
            elif reply[1] == 'e':
                return 'm'
        else:
            return 'err'


def int_check(question, low_num):
    error = "Please enter a valid number higher than {}".format(low_num)

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            value_1 = float(input(question))

            if value_1 > low_num:
                valid = True
                return value_1

            else:
                print(error)

        # if integer is not entered, display an error message
        except ValueError:
            print(error)


def find_area(name):
    c = 0
    while c < len(shapes_list):
        if shapes_list[c] == name:
            shape = shapes_list[c]
            if shape == 'square':
                square_l = int_check("Please enter your length: ", 0)
                square_w = int_check("Please enter your width: ", 0)
                return square_area(square_l, square_w)

            elif shape == 'circle':
                circle_r = int_check("Please enter your radius: ", 0)
                return circle_area(circle_r)
            elif shape == 'trapezium':
                trapezium_a = int_check("Please enter your A: ", 0)
                trapezium_b = int_check("Please enter your B: ", 0)
                trapezium_h = int_check("Please enter your height: ", 0)
                return trapezium_area(trapezium_a, trapezium_b, trapezium_h)
            elif shape == 'triangle':
                triangle_b = int_check("Please enter in your base: ", 0)
                triangle_h = int_check("Please enter in your height: ", 0)
                return triangle_area(triangle_b, triangle_h)
            elif shape == 'rhombus':
                rhombus_p = int_check("Please enter in your P: ", 0)
                rhombus_q = int_check("Please enter in your Q: ", 0)
                return rhombus_area(rhombus_p, rhombus_q)
            elif shape == 'kite':
                kite_p = int_check("Please enter in your P: ", 0)
                kite_q = int_check("Please enter in your Q: ", 0)
                return kite_area(kite_p, kite_q)
        else:
            c += 1


def square_area(b, h):
    return b * h


def rectangle_area(b, h):
    return b * h


def circle_area(r):
    return 3.141 * r * r


def triangle_area(b, h):
    return b / 2 * h


def trapezium_area(a, b, h):
    return (a + b) / 2 * h


def rhombus_area(p, q):
    return p * q / 2


def kite_area(p, q):
    return p * q / 2


shape_name = shape_select('Please enter in a shape: ')

# if shape name is not valid, loop through and continue asking user what shape to identify until valid shape is entered
if shape_name == 'err':
    name_valid = False
    while not name_valid:
        shape_name = shape_select('Please enter in a shape: ')
        if shape_name != 'err':
            name_valid = True

shape_units = units_select('Please enter in a unit of measurement: ')

# if shape units is not valid, loop through and continue asking user what units to identify until valid unit is entered
if shape_units == 'err':
    units_valid = False
    while not units_valid:
        shape_units = units_select('Please enter in a unit of measurement: ')
        if shape_units != 'err':
            units_valid = True

print('Your area is:', find_area(shape_name), shape_units + '^2')
