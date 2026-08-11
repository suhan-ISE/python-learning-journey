# Arbitrary Arguments (Variable-Length):
# When you do not know in advance how many arguments will be passed into your function,
#                      you can use arbitrary arguments.

# 1. Arbitrary Positional Arguments (*args)
# Using a single asterisk (*) groups an unknown number of positional arguments
#                   into a tuple.

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))

# 2.Arbitrary Keyword Arguments (**kwargs)
# Using a double asterisk (**) groups an unknown number of keyword arguments
#                    into a dictionary.

def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_profile(username="coder12", role="Admin", status="Active")

# When combining multiple argument types in a single function,
# they must follow a specific order in both the definition and the call:
# Positional arguments → Keyword/Default arguments → *args → **kwargs.

