# module = a file containing code you want to include in program use 'import' to
# include a module (built-in or your own) useful to breakup a large program into
# reusable separate file.

pi =3.14159

def square(x):
    return x*x
def cube(x):
    return x*x*x
def circumference(radius):
    return 2*pi*radius
def area(radius):
    return pi*radius**2
def rectangle(width, height):
    return width*height