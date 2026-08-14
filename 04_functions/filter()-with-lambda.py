"""How Filter Works
The filter() function passes every item into a condition function.
 If the function returns True, the item stays;
  if it returns False, the item is discarded.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only the even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
print(evens)
print(list(evens))
# Output: [2, 4 ......]
