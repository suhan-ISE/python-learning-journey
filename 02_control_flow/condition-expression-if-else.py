#condition expression = a one line shortcut for the if-else statement (ternary operator)
# print or assign one of two values based on a condition.
# x if condition else y

while True:   # while loop to repeat excecution until it breaks
    value = input("enter a number (q/quit) to exit:")
    if value in ("q", "quit"):
        break
    num = int(value)
    print("positive" if num >= 0 else "negative") # condition expression

