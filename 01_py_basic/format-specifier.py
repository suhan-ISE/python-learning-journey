#format specifier = {values : flages} formate a value based on what flages are inserted.

# 1. Floating-Point Precision (.2f)
# Formats a float to exactly 2 decimal places
pi = 3.14159265
print(f"1. Pi to 2 decimal places: {pi:.2f}")
print(f"1. Pi to 2 decimal places: {pi:.4f}") # exactly to 4 decimal places

# 2. Number Width and Padding (05d)
# Pads an integer with leading zeros to make it 5 characters wide
id = 69
print(f"2. Padded User ID: {id:05d}")

# 3. Thousands Separator (,)
# Adds commas to large numbers for readability
population = 1250034688
print(f"3. Formatted Population: {population:,}")

# 4. Percentage (%)
# Multiplies by 100 and formats as a percentage
score = 0.856
print(f"4. Test Score: {score:.1%}")

# 5. Scientific Notation (e)
# Displays numbers in exponential format
big_num = 9876543210
print(f"5. Scientific Notation: {big_num:.2e}")

# 6. Base Conversions (b, o, x)
# Converts integers to binary, octal, or hexadecimal
number = 1024
print(f"6. Binary: {number:b} | Octal: {number:o} | Hex: {number:x}")

# 7. Text Alignment and Custom Width (<, >, ^)
# Formats string spacing and alignment within a set block width
name = "Alice"
print(f"7. Left-aligned  : '{name:<10}'")
print(f"   Right-aligned : '{name:>10}'")
print(f"   Center-aligned: '{name:^10}'")

# 8. indicate positive values (+)
# 9. insert a space before positive numbers ( )

