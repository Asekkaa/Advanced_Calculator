import math


def advanced_calculator():
    print("Advanced Calculator")
    print("Supported operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (sqrt)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log)")
    print("11. Factorial (factorial)")
    print("Type 'q' to exit.")

    while True:
        # Ask the user to select an operation
        operation = input("\nChoose an operation (1-11 or 'q' to quit): ").strip()

        if operation == 'q':
            print("Shutting down the calculator.")
            break

        # Check for operations that require two inputs (e.g., addition, multiplication)
        if operation in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if operation == '1':
                    result = num1 + num2
                elif operation == '2':
                    result = num1 - num2
                elif operation == '3':
                    result = num1 * num2
                elif operation == '4':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                        continue
                    result = num1 / num2
                elif operation == '5':
                    result = math.pow(num1, num2)

                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid input, please enter numeric values.")

        # Check for operations that require one input (e.g., square root, trigonometric functions)
        elif operation == '6':
            try:
                num = float(input("Enter the number: "))
                result = math.sqrt(num)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid input, please enter a valid number.")

        elif operation == '7':
            try:
                num = float(input("Enter the angle in radians: "))
                result = math.sin(num)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid input, please enter a valid number.")

        elif operation == '8':
            try:
                num = float(input("Enter the angle in radians: "))
                result = math.cos(num)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid input, please enter a valid number.")

        elif operation == '9':
            try:
                num = float(input("Enter the angle in radians: "))
                result = math.tan(num)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid input, please enter a valid number.")

        elif operation == '10':
            try:
                num = float(input("Enter the number: "))
                base = input("Enter the logarithm base (default: e): ").strip()
                if base == '':
                    result = math.log(num)
                else:
                    base = float(base)
                    result = math.log(num, base)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid input, please enter valid numbers.")

        elif operation == '11':
            try:
                num = int(input("Enter a number: "))
                result = math.factorial(num)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid input, please enter a non-negative integer.")
            except OverflowError:
                print("Error: The number is too large to calculate.")

        else:
            print("Error: Invalid operation selection.")


advanced_calculator()
