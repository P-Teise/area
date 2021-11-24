shapes_list = ['square', 'circle', 'trapezium', 'triangle', 'rhombus', 'kite', 'rectangle']


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


shape_name = shape_select('Please enter in a shape: ')

# if shape name is not valid, loop through and continue asking user what shape to identify until valid shape is entered
if shape_name == 'err':
    name_valid = False
    while not name_valid:
        shape_name = shape_select('Please enter in a shape: ')
        if shape_name != 'err':
            name_valid = True
            print("Answer OK you said:", shape_name)
