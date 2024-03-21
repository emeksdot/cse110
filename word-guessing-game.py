"""
A Word Guessing game created by Emeka Thomas Onwugbonu
on March 21, 2024 for the CSE 110 Course at BYU Idaho
"""

secret_word = input("Enter secret word: ")
number_of_guesses = 0
guess_word = input("Guess a word: ")
number_of_guesses = number_of_guesses + 1

while(secret_word.lower() != guess_word.lower()):
    number_of_guesses = number_of_guesses + 1
    guess_word = input("Make another guess?: ")   
    if(secret_word.lower() == guess_word.lower()):
        break

if(number_of_guesses == 1 ):
    print(f"You guessed it! After {number_of_guesses} attempt.")
else:
    print(f"You guessed it! After {number_of_guesses} attempts.")



