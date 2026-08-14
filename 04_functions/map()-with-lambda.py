""" How Map Works
The map() function passes every item from your iterable into a
function and collects the updated results.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Double every single number
squared = map(lambda x: x * 2, numbers)
print(squared)
print(list(squared))
# Output: [2, 4, 6, 8 .....]

"""The "Boolean Trap" (Common Mistake)If you pass a logical condition into map(), 
it will not filter your list. Instead, it transforms your data into an array of Booleans.
"""
numbers = [1, 2, 3, 4]

# Using map with a condition returns the True/False results!
mistake = list(map(lambda x: x % 2 == 0, numbers))
print(mistake)
# Output: [False, True, False, True]
