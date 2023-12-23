# Defining and Calling Functions
# Function to greet a user
def greet(name):
    """ Return a greeting message. """
    return f"Hello, {name}!"

# Calling the function with the argument "Alice"
print(greet("Alice"))  # Outputs: Hello, Alice!

# Parameters and Arguments
# Function to calculate the area of a rectangle
def calculate_area(length, width):
    """ Calculate area of a rectangle. """
    return length * width

# Calling the function with parameters 10 and 5
print(calculate_area(10, 5))  # Outputs: 50

# Return Values
# Function to check if a number is even
def is_even(number):
    """ Return True if number is even, else False. """
    return number % 2 == 0

# Checking if 4 is even
print(is_even(4))  # Outputs: True

# Default Parameter Values
# Function with a default parameter value
def send_message(message, sender="Admin"):
    """ Print a message from a sender. Default sender is 'Admin'. """
    print(f"From {sender}: {message}")

# Calling function without specifying sender
send_message("Server starting")  # Outputs: From Admin: Server starting

# Keyword Arguments
# Calling a function using keyword arguments
def create_user(name, age, job):
    """ Create a user with name, age, and job. """
    print(f"Name: {name}, Age: {age}, Job: {job}")

# Using keyword arguments to specify values out of order
create_user(age=30, name="Bob", job="Developer")

# Variable-length Arguments (*args and **kwargs)
# Function accepting variable number of arguments
def log_message(*args, **kwargs):
    """ Log a message with optional additional information. """
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Logging an error with additional details
log_message("Error occurred", time="10:00", severity="High")

# Nested Functions
# A function that contains another function
def outer_function(text):
    """ Outer function containing an inner function. """
    def inner_function():
        """ Inner function that uses the 'text' parameter. """
        return f"Inner says: {text}"
    return inner_function()

# Calling the outer function
print(outer_function("Hello!"))  # Outputs: Inner says: Hello!

# Lambda Functions
# A simple lambda function to double a number
double = lambda x: x * 2
# Using the lambda function
print(double(5))  # Outputs: 10

# Functional Programming Tools - map()
# Using map() with a lambda function to square numbers
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
# Printing the squared numbers
print(list(squared))  # Outputs: [1, 4, 9, 16]

# Recursive Functions
# A recursive function to calculate factorial of a number
def factorial(n):
    """ Return the factorial of n using recursion. """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calculating the factorial of 5
print(factorial(5))  # Outputs: 120
