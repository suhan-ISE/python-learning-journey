# using function as argument
def add(num):
    return num + 1

def square(num):
    return num ** 2

num = int(input("Enter a number: "))
result = square(add(num)) # using function in-terms of argument inside another function.
print(result)