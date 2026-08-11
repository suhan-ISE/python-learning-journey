# a set is an unordered collection of unique items.
# No Duplicates: Duplicate elements are discarded automatically.
# Unordered: Items have no fixed position;
# you cannot access them using indexes (like my_set[0]).
# Set elements must be immutable: You can put numbers, strings, or tuples inside a set,
#                                 but you cannot put lists or dictionaries inside it.

# 1. How to create sets
# Use curly braces for non-empty sets
fruits = {"apple", "banana", "cherry", "apple"}  # "apple" is a duplicate and will be removed automatically

print("Initial set (duplicates removed):", fruits)

# 2. Adding and removing elements
fruits.add("orange")        # Adds a single item
fruits.remove("banana")     # Removes "banana" (Raises KeyError if not found)
fruits.discard("grapes")    # Safely removes "grapes" (Does nothing if not found)

print("Modified set:", fruits)

# 3. Mathematical Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (All unique elements from both sets)
print("Union:", set_a | set_b)

# Intersection (Elements present in both sets)
print("Intersection:", set_a & set_b)

# Difference (Elements in set_a but not in set_b)
print("Difference (A - B):", set_a - set_b)

# Symmetric Difference (Elements in either set, but not both)
print("Symmetric Difference:", set_a ^ set_b)
