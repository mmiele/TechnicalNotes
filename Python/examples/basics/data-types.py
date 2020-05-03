"""
.. module:: data-types
    :platform: OS X
    :synopsis: Shows how to use important data types

.. moduleauthor:: Michael <milexm@gmail.com>

.. note::
    Every value in Python has a datatype. Because everything is an object in Python,
    data types are classes and variables are instances (object) of these classes.
    There are various data types in Python.

    Run it:
    In a terminal winodow at the command prompt enter: > python simple_calculator.py.
    Enter the operation selection, then the first and second operand.

"""

def number_types():
    ''' Shows types of numbers.

    .. note::
        Integers, floating point numbers and complex numbers fall under Python numbers category.
        They are defined as int, float and complex classes in Python.
        We can use the type() function to know which class a variable or a value belongs to.
        Similarly, the isinstance() function is used to check if an object belongs to a particular class.
   '''
    a = 5
    print(a, "is of type", type(a))

    a = 2.0
    print(a, "is of type", type(a))

    a = 1+2j
    print(a, "is complex number?", isinstance(1+2j,complex))


def list_types():
    ''' Shows list type.

    .. note::
        List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible.
        All the items in a list do not need to be of the same type.
        Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ].
   '''
    # Define a list
    a = [5,10,15,20,25,30,35,40]

    '''
    Use the slicing operator [ ] to extract an item or a range of items from a list.
    The index starts from 0 in Python.
    '''
    # a[2] = 15
    print("a[2] = ", a[2])

    # a[0:3] = [5, 10, 15]
    print("a[0:3] = ", a[0:3])

    # a[5:] = [30, 35, 40]
    print("a[5:] = ", a[5:])


# Display menu.
print("Select operation.")
print("n Numbers")
print("l Lists")

print("quit")



# Perform operations until the user quits.
while True:
    # Take input from the user
    choice = input("Enter choice(n quit): ")

    # Check if choice is one of the four options
    if choice in ('n', 'l'):
        if choice == 'n':
            number_types()
        elif choice == 'l':
            list_types()
    else:
        if choice == 'quit':
            print("Bye")
            break
        else:
            print("Invalid Input")