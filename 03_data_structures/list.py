#collections = single "variable" used to store multiple values.
#list = [] ordered and changeable ,Duplicates ok.
#set = {} unordered and immutable ,but add/remove ok , No Duplicates.
#Tuple = () ordered and unchanged ,Duplicates Ok , faster.

# lists methods : create,modify and manage lists by Built-in Methods.

# 1. Creating a List
fruits = ["apple", "banana", "cherry" , "kiwi"]
print("Original list:", fruits)

# 2. Accessing Items (Zero-based indexing)
print("First item:", fruits[0])
print("Last item:", fruits[-1])

#2. slicing : Accessing specific range of items
print("first 3 items:", fruits[:3]) #[ : 2 ] means accessing items from index 0 to 2
print("last 3 items:", fruits[-3:]) # accessing items from index -3(3rd last) to end

# 3. Adding Items
fruits.append("orange")         # Adds to the end
fruits.insert(1, "mango")       # Inserts 'mango' at index 1
print("After adding items:", fruits)

# 4. Combining Lists
tropical = ["pineapple", "papaya"]
fruits.extend(tropical)         # Merges 'tropical' into 'fruits'
print("After extending:", fruits)

# 5. Removing Items
fruits.remove("banana")         # Removes the first occurrence of 'banana'
popped_item = fruits.pop(2)     # Removes and returns the item at index 2
print(f"Removed item: {popped_item}")
print("After removing items:", fruits)

# 6. Finding and Counting Elements
index_of_kiwi = fruits.index("kiwi")
kiwi_count = fruits.count("kiwi")
print(f"'kiwi' is at index {index_of_kiwi} and appears {kiwi_count} time(s)")

# 7. Sorting and Reversing
fruits.sort()                   # Sorts alphabetically in-place
print("Sorted list:", fruits)

fruits.reverse()                # Reverses the order in-place
print("Reversed list:", fruits)

# 8. Finding List Length
print("Total number of items:", len(fruits))

#9. clear list
fruits.clear()
print("After clearing items:", fruits)
