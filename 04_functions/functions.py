# a "function" is a reusable block of code that executes only when it is called.
# You define a function using the 'def' keyword.

# 1. Basic Function Syntax

# Define the function
def greet():
    print("Hello! Welcome to Python World.")

# Call the function to run it
greet()

# 2. Function with Parameters (Inputs)

# 'name' and 'age' are the parameters
def greet_user(name , age):
    print(f"Hello! i'm {name} i'm {age} years old")

# Pass "suhan" and 20 as the arguments
greet_user(name="suhan" , age=20)

# 3. Function with a Return Value
def add_numbers(a, b):
    return a + b

# Store the returned result in a variable
result = add_numbers(5, 7)
print("The sum is:", result)

# 4. Function with Default Arguments

# 'country' defaults to "India" if not provided
def display_origin(name, country="India"):
    print(f"{name} is from {country}.")

display_origin("suhan")            # Uses default: suhan is from India.
display_origin("Joy", "USA")      # Overrides default: Joy is from USA.

