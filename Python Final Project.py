import math

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Function to calculate sine
def sine(x):
    return math.sin(math.radians(x))

# Function to calculate cosine
def cosine(x):
    return math.cos(math.radians(x))

# Function to calculate tangent
def tangent(x):
    return math.tan(math.radians(x))

# Function to calculate square root
def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Cannot take the square root of a negative number."

# Function to calculate factorial
def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number is undefined."
    else:
        return math.factorial(x)

# Main function to introduce the calculator and the difference operations available
def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Sine (sin)")
    print("6. Cosine (cos)")
    print("7. Tangent (tan)")
    print("8. Square Root (sqrt)")
    print("9. Factorial (fact)")

    while True: #starts an infinite loop that will continue until the usar exits
        try:
            operation = input("Enter operation (or 'quit' to exit): ").lower() #Gives usar the option to add an input that was listed above

            if operation == 'quit': #Gives usar the option to exit
                print("Exiting the calculator. Goodbye!")
                return  # Exit the calculator function completely, breaking the loop

            if operation in ['+', '-', '*', '/']: #Check if the operation is basic arithmeitc
                x = float(input("Enter the first number: ")) #Asks usar to give two number to use to perform the operation
                y = float(input("Enter the second number: "))

                if operation == '+': #Explains what to do with x and y based on the type of math being performed
                    print(f"{x} + {y} = {add(x, y)}") #Add function
                elif operation == '-':
                    print(f"{x} - {y} = {subtract(x, y)}") #Subtract function
                elif operation == '*':
                    print(f"{x} * {y} = {multiply(x, y)}") #Multiply function
                elif operation == '/':
                    print(f"{x} / {y} = {divide(x, y)}") #Divide function

            elif operation in ['sin', 'cos', 'tan']: #Check for trgionometric functions
                x = float(input("Enter the angle in degrees: "))
                if operation == 'sin':
                    print(f"sin({x}) = {sine(x)}") #Sine
                elif operation == 'cos':
                    print(f"cos({x}) = {cosine(x)}") #Cosine
                elif operation == 'tan':
                    print(f"tan({x}) = {tangent(x)}") #Tangent

            elif operation == 'sqrt': #Check if the operation is a square root
                x = float(input("Enter the number to find the square root: "))
                print(f"sqrt({x}) = {square_root(x)}") #Gives the sqaure root for the given input x

            elif operation == 'fact': #Check if the operation is a factorial 
                x = int(input("Enter a number to find the factorial: "))
                print(f"{x}! = {factorial(x)}") #Gives the factorial for the given input x

            else:
                print("Invalid operation! Please choose a valid operation.") #If an operation is not recognized
        
        except ValueError:
            print("Invalid input! Please enter valid numbers.") #If the input is an invalid number
        
        print("\n") #Print a blank line to separate different inputs for clarity

# Run the calculator function
if __name__ == "__main__":
    calculator()
