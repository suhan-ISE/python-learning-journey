# Dictionary :
# Syntax: Use curly braces {} with key: value pairs separated by commas.
# Keys: Must be unique and immutable types (like strings, numbers, or tuples).
# Values: Can be anything (lists, strings, integers, or even other dictionaries).

# 1. Creating a dictionary
# Keys are unique (e.g., "name"), and values can be any data type
student = {
    "name": "suhan khan",
    "age": 20,
    "major": "Information Science and Engineering",
    "cgpa": 8.2
}
print("Initial Dictionary:", student)

# 2. Accessing values
# Using square brackets (can cause error if key is missing)
print("Student Name:", student["name"])

# Using .get() method (safer, returns None if key doesn't exist)
print("Student Age:", student.get("age"))
print("Scholarship Status:", student.get("has_scholarship", "Not Found"))

# 3. Adding or Updating items
student["cgpa"] = 8.9               # Updates existing key
student["graduation_year"] = 2029  # Adds a brand new key-value pair
print("\nAfter Update and Addition:", student,end=" ")
print()
# 4. Checking if a key exists
if "major" in student:
    print(f"Yes, 'major' is a key in the dictionary. Value: {student['major']}")

# 5. Iterating (looping) through a dictionary
print("\n--- Dictionary Iteration ---")
# Looping through keys and values simultaneously using .items()
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")

# 6. Removing items
removed_value = student.pop("age")  # Removes key and returns its value
print(f"\nRemoved Age: {removed_value}")

del student["cgpa"]                 # Deletes key permanently
print("After Deletions:", student)

# 7. Built-in views
print("Remaining Keys:", student.keys())    # Get all keys
print("Remaining Values:", list(student.values())) # Get all values
