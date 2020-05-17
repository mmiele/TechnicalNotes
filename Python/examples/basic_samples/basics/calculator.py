"""Test in calculator.py.
"""

import re

class Calculator(object):
    """Calculator class."""
    pass

    def performCalculation():
        """This is the performCalculation docstring."""
        global run
        global previous

        equation = ""

        while run:
            if previous == 0:
                equation = input("Enter equation: ")
            else:
                equation = input(str(previous))

            if equation == 'quit':
                print("Goodbye")
                run = False
            else:
                equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)

    def main():
        performCalculation()

    if __name__ == "__main__":
        main()
