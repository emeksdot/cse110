"""
A Guessing Game Program created by Emeka Thomas Onwugbonu
on March 20, 2024
"""
import random

# number = random.randint(1, 15)
# print(number)

magic_number = int(input("What is the magic number?: "))
guess = int(input("What is your guess?: "))
# Additional line
number_of_guesses = 1

# if(magic_number > guess):
#     print("Higher")
# elif(magic_number < guess):
#     print("Lower")
# else:
#     print("You guessed it!")

while(magic_number != guess):
    number_of_guesses = number_of_guesses + 1
    if(magic_number > guess):
        print("Higher")
    elif(magic_number < guess):
        print("Lower")
    guess = int(input("What is your guess?: "))
print(f"You guessed it! After {number_of_guesses} attempts.")
