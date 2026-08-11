# variable scope  refers to the specific region of a program where a variable is visible and accessible.

# "Scope resolution" is the process and set of rules Python uses to search for and
#    locate a variable name when it is referenced in your code.

# The LEGB Scope Resolution Rule
# Local: Variables defined inside the current function.
# Enclosing: Variables inside any outer, enclosing functions (nested functions).
# Global: Variables defined at the top-most level of the script or module.
# Built-in: Special names reserved by Python (like print, len, or ValueError)

# 'Comprehensive Example'
# The script below demonstrates all four layers of the LEGB rule executing simultaneously.

# 4. BUILT-IN SCOPE (B)
# 'len' is a built-in Python function automatically available anywhere.

# 3. GLOBAL SCOPE (G)
message = "I am Global"


def outer_function():
    # 2. ENCLOSING SCOPE (E)
    message = "I am Enclosing"

    def inner_function():
        # 1. LOCAL SCOPE (L)
        message = "I am Local"

        print(message)  # Looks up Local -> Prints: "I am Local"
        print(len(message))  # Looks up Local -> Enclosing -> Global -> Built-in -> Prints: 10

    inner_function()


outer_function()
print(message)  # Looks up Global -> Prints: "I am Global"
