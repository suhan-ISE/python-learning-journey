#nested loop = a loop within another loop (outer,inner)
#   outer loop:
#        innerloop:

for x in range(3):         # act as row
    for y in range(1,10):  # act as column
        print(y, end=" ")
    print()
print()
# create 'symbols' square or rectangle
rows = int(input("How many rows would you like? "))
columns = int(input("How many columns would you like? "))
symbol = input("enter a symbol")

for row in range(rows):
    for column in range(columns):
        print(symbol, end=" ")
    print()

