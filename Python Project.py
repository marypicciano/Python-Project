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

# Main function to handle the user interface
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
