# functions go here
units_short = ['mm', 'cm', 'm', 'km', 'ft', 'in']
units_long = ['millimetre', 'centimetre', 'metre', 'kilometre', 'feet', 'inches']


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


shape_units = units_select('Please enter in a unit of measurement: ')

# if correct units are entered, notify user of input
if shape_units != 'err':
    print("Answer OK, you said:", shape_units)
# if shape units is not valid, loop through and continue asking user what units to identify until valid unit is entered
if shape_units == 'err':
    units_valid = False
    while not units_valid:
        shape_units = units_select('Please enter in a unit of measurement: ')
        if shape_units != 'err':
            units_valid = True
            print("Answer OK, you said:", shape_units)

