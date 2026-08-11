# a list comprehension offers a shorter, cleaner syntax to create a new list
#                  based on the values of an existing iterable.
# It essentially replaces a multi-line for loop with a single line of code.
# syntax = new_list = [expression for item in iterable if condition]

# 1. Basic Transformation (Squaring Numbers)

# Traditional Way (3 lines)
squares = []
for x in range(1, 6):
    squares.append(x**2)
print(squares)  # Output: [1, 4, 9, 16, 25]

# List Comprehension Way (1 line)
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# 2. Filtering with an if Condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filters out odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# 3. Using if-else Conditions

numbers = [1, 2, 3, 4, 5]
# Labels numbers as 'Even' or 'Odd'
labels = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(labels)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

