#while loop for user input ,where user gives the input until the
#                         condition is satisfied.

secret_word = "python"
guess = ""

# Keep asking the user until they guess the correct word

while guess.lower() != secret_word:
    guess = input("Guess the secret word: ")

print("You got it right!")