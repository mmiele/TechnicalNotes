# ---------------------------------------------------------
# Copyright (c) MSSC
# ---------------------------------------------------------

"""
In this module, you will learn to manipulate date and time in Python.
"""

from datetime import datetime

class MyDateTime(object):

    def current_date_time(self, choice):
        """
        Displays the current time. It also calculates the related time stamp.
        Then converts the time stamp to date and time.

        .. remarks::
            This function imports the :class:`datetime` from the datetime module. Then, it uses the :meth: `now()`
            to get a datetime object containing current date and time.
            Using datetime.strftime() method, it then creates a string representing the current time.

        """

        if choice in ('dt', 'ts', 'dtts'):

            # Get current date and time.
            now = datetime.now()
            # Get the time stamp.
            timestamp = datetime.timestamp(now)

            if choice == 'dt':
                # Display current date and time.
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                print("current date and time =",date_time)
            elif choice == 'ts':
                # Dispay the time stamp.
                print("time stamp =", timestamp)
            elif choice == 'dtts':
                # Get current date and time from the time stamp.
                # and display the result.
                dt_object = datetime.fromtimestamp(timestamp)
                print("(dt_object - date and time from time stamp =", dt_object)
                print("type(dt_object) =", type(dt_object))
        else:
            print("invalid choice")

    def menu(self):
        # Display menu.
        print("Make your choice:")
        print("{:>20}".format("dt   - Date & Time"))
        print("{:>19}".format("ts   - Time Stamp"))
        print("{:>36}".format("dtts - Date & Time from Time Stamp"))
        print("{:>21}".format("m    - Display Menu"))
        print("{:>13}".format("q    - Quit"))


def main():
    ''' Main function,
        It displays the menu. Then enter a loop until the user exit.
    '''
    # Instantiate MyDateTime class.
    date_time = MyDateTime()

    # Display menu.
    date_time.menu()

    # Perform operations until the user quits.
    while True:
        # Get input from the user
        choice = input("Choice: ").lower()

        # Check if choice is one of the four options
        if choice in ('dt', 'ts', 'dtts'):
            date_time.current_date_time(choice)
        elif choice == 'm':
           # Display menu:
           date_time.menu()
        else:
            if choice == 'q':
                print("Bye")
                break
            else:
                print("Invalid Input")


if __name__ == "__main__":
    main()
