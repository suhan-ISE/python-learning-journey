# A tuple is an ordered collection of items that is immutable
# (cannot be changed after creation).
# Parentheses () are typically used to create tuples,
# but the separating commas , are what actually make it a tuple.
# Single item tuples must include a trailing comma (e.g., (50,)).
# Without it, Python views it as a regular integer or string inside parentheses.
# Immutability makes tuples faster than lists and safe from accidental data modification.

# 1. Creating Tuples
empty_tuple = ()
mixed_tuple = ("Python", 3, 4.5, True)  # Can hold different data types
single_item_tuple = (50,)  # Trailing comma is required for a single item

print("--- 1. Creating Tuples ---")
print("Mixed Tuple:", mixed_tuple)
print("Single Item Tuple Type:", type(single_item_tuple))


# 2. Accessing Elements (Zero-based indexing)
fruits = ("apple", "banana", "cherry", "date")

print("\n--- 2. Accessing Elements ---")
print("First element (index 0):", fruits[0])
print("Last element (index -1):", fruits[-1])
print("Slicing (index 1 to 3):", fruits[1:3])


# 3. Tuple Unpacking
# Extracting individual items from a tuple and assigning them to variables
coordinates = (10, 20, 30)
x, y, z = coordinates

print("\n--- 3. Tuple Unpacking ---")
print(f"X: {x}, Y: {y}, Z: {z}")


# 4. Built-in Tuple Methods
numbers = (1, 2, 3, 2, 4, 2, 5)

print("\n--- 4. Built-in Methods ---")
print("Total number of elements (len):", len(numbers))
print("Count how many times '2' appears:", numbers.count(2))
print("Find the index of '4':", numbers.index(4))


# 5. Proof of Immutability (Will raise an error)
print("\n--- 5. Immutability Proof ---")
try:
    fruits[0] = "blueberry"  # This is illegal
except TypeError as error:    #expecting the error so that our program don't get crash.
    print("Error caught successfully:", error)
