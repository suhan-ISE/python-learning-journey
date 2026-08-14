""" Recursion is a process in which a function calls itself till a certain condition is not met
factotial of n => n * (n-1) * (n-2) * ...... 2 * 1
n!
4! = 4 * 3 * 2 * 1 = 24
"""
# without recursion:
def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1

    return factorial
num = 4
print(f" factorial of given num recursion is ={fact(num)}")

# with recursion :
def fact(num):
    if num == 1:
        return 1
    else:
        factorial = num * fact(num - 1)
        return factorial
num = 4
print(f" factorial of given num with recursion is ={fact(num)}")