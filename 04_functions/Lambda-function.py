# lambda function
# syntax
# lambda argument : expression

# without lambda
def square(num):
    return num ** 2
res = square(5)
print(f"square of given num without lambda function is : {res}")

#with lambda:

fun = lambda x : x ** 2
res = fun(4)
print(f"square of given num lambda function is : {res}")