# ---------------------------------------------------------
# Copyright (c) MSSC
# ---------------------------------------------------------

"""
In this module, you will learn to manipulate date and time in Python.
"""

from datetime import datetime

class MyDateTime(object):

    def get_current_date_time(self, choice):
        """
        Displays the current time. It also calculates the related time stamp.
        Then converts the time stamp to date and time.

        :param choice: The user's selection
        :type choice: str

        .. remarks::

            This function imports the :class:`datetime` from the datetime module.
            Then, it uses the :meth: `now()` to get a datetime object containing
            current date and time. Using datetime.strftime() method, it then creates
            a string representing the current time.

            .. note::

                This is a highlighted note in a box

        """

        if choice in ('1', '2', '3'):

            # Get current date and time.
            now = datetime.now()
            # Get the time stamp.
            timestamp = datetime.timestamp(now)

            if choice == '1':
                # Display current date and time.
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                print("current date and time =",date_time)
            elif choice == '2':
                # Dispay the time stamp.
                print("time stamp =", timestamp)
            elif choice == '3':
                # Get current date and time from the time stamp.
                # and display the result.
                dt_object = datetime.fromtimestamp(timestamp)
                print("(dt_object - date and time from time stamp =", dt_object)
                print("type(dt_object) =", type(dt_object))
        else:
            print("invalid choice")


    def get_datetime_from_string(self, date_string):
        """
        Get a datetime object from a string.

        .. remarks::
            This function use the :meth:`datetime.now().strftime() method which takes two arguments:
                - string (to be converted to datetime)
                - format code
            Based on the string and format code, the method returns its equivalent datetime object.
            For more information, see `Python strptime() <https://www.programiz.com/python-programming/datetime/strptime>`

            .. note::
                You cannot create datetime object from every string. The string needs to be in a certain format.

            :param date: The string containing date and time
            :type my_public_param: str

            :return: datetime object
            :rtype: :class:`datetime.datetime` object

        """
        print("date_string =", date_string)
        print("type of date_string =", type(date_string))

        date_object = datetime.strptime(date_string, "%d %B, %Y")

        return date_object


    def menu(self):
        """ Display menu."""

        print("1 - Date & Time")
        print("2 - Time Stamp")
        print("3 - Date & Time from Time Stamp")
        print("4 - Date & Time from String")
        print("m - Display Menu")
        print("q - Quit")


def main():
    ''' Main function.
        It displays the menu. Then enter a loop until the user exits.
    '''

    # Instantiate MyDateTime class.
    date_time = MyDateTime()

    date_time.menu()

    # Perform operations until the user quits.
    while True:
        try:
            choice = input("Enter your choice: ").lower()
            # Check if choice is one of the four options
            if choice in ('1', '2', '3'):
                date_time.get_current_date_time(choice)
            elif choice == '4':
                date_object = date_time.get_datetime_from_string("21 June, 2018, 09:15:32")
                print("date_object =", date_object)
                print("type of date_object =", type(date_object))
            elif choice == 'm':
                # Display menu:
                date_time.menu()
            else:
                if choice == 'q':
                    print("Bye")
                    break
        except ValueError:
            print("Invalid choice.")
            main()
    exit

if __name__ == "__main__":
    main()
