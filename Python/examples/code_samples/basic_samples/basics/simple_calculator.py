"""Test in simple_calculator.py
"""

class SimpleCalculator(object):
    """Docstring for simple calculator."""
    pass

    def add(x, y):
        """
        Adds two numbers

        :param int x: first operand
        :param int y: second operand
        :return: the operation result
        :rtype: int
        :raises ValueError: if could not convert operand to float
        """
        return x + y

    def subtract(x, y):
        """
        Subtracts two numbers

        :param int x: first operand
        :param int y: second operand
        :return: the operation result
        :rtype: int
        :raises ValueError: if could not convert operand to float
        """
        return x - y


    def multiply(x, y):
        """
        Multiplies two numbers

        :param int x: first operand
        :param int y: second operand
        :return: the operation result
        :rtype: int
        :raises ValueError: if could not convert operand to float
        """
        return x * y


    def divide(x, y):
        """
        Divides two numbers

        :param int x: first operand
        :param int y: second operand
        :return: the operation result
        :rtype: int
        :raises ValueError: if could not convert operand to float
        """
        return x / y

    def main():

        # Display menu.
        print("Select operation.")
        print("+ Add")
        print("- Subtract")
        print("* Multiply")
        print("/ Divide")
        print("quit")

        # Perform operations until the user quits.
        while True:
            # Take input from the user
            choice = input("Enter choice(* - * / quit): ")

            # Check if choice is one of the four options
            if choice in ('+', '-', '*', '/'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '+':
                    print(num1, "+", num2, "=", add(num1, num2))

                elif choice == '-':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == '*':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '/':
                    print(num1, "/", num2, "=", divide(num1, num2))
            else:
                if choice == 'quit':
                    print("Bye")
                    break
                else:
                    print("Invalid Input")

    if __name__ == "__main__":
        main()