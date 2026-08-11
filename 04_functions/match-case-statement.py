# Match case statement:a powerful structural pattern matching tool that offers a
# cleaner, more readable alternative to complex if-elif-else chains.

# Basic Syntax Example

def check_http_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case _:             # wildcard: Acts as a default "catch-all" handler.
            return "Unknown Status Code"

# Test the function
print(check_http_status(200))
print(check_http_status(404))
print(check_http_status(500))

# Advanced Usage Examples

# 1. Matching Multiple Values (OR Operator)
def get_weekend_status(day):
    match day.lower():
        case "saturday" | "sunday":
            return "It's the weekend!"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "It's a workday."
        case _:
            return "Invalid day."


# 2. Adding Conditions

def process_number(n):
    match n:
        case int() if n > 0:    # if statement
            return f"{n} is a positive integer"
        case int() if n < 0:
            return f"{n} is a negative integer"
        case 0:
            return "Zero"
        case _:
            return "Not an integer"