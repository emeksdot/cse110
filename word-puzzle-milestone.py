"""
A Word Guessing game created by Emeka Thomas Onwugbonu
on March 22, 2024 for the CSE 110 Course Milestone Project at BYU Idaho
The aim of the game is to guess the name of the Prophets in the Book of Mormon, from 1 Nephi to Omni from a list gotten from Wikipedia (https://en.wikipedia.org/wiki/List_of_Book_of_Mormon_prophets)

"""
import random

name = input("Enter your first name: ")
print(f"Welcome {name.capitalize()} to The Book of Mormon Prophet's name guessing game Version-1")

list_of_prophets = ["Lehi",
"Nephi", "Jacob", "Enos", "Jarom", "Omni", "Amaron", "Chemish", "Abinadom", "Amaleki", "Neum", "Zenos", "Zenock"
]

number = random.randint(0, len(list_of_prophets))

secret_word = list_of_prophets[number]
hint = "_" * len(secret_word)
print(f"Your hint is: {hint}")
number_of_guesses = 0
guess_word = input("Guess a word: ")
number_of_guesses = number_of_guesses + 1

secret = secret_word.lower()
guess = guess_word.lower()


while(secret != guess):
    if(len(secret) != len(guess)):
        # number_of_guesses = number_of_guesses + 1
        print(f"Sorry your guess must have the same number of letters as the secret word.")

    if(len(secret) == len(guess)):        
        for i in range(len(guess)):
            if(guess[i] == secret[i]):
                print(guess[i].upper(), end="")
            elif(guess[i] != secret[i] and guess[i] in secret):
                print(guess[i].lower(), end="")
            else:
                print("_", end="")



    print()
    
    if(secret == guess):
        print(guess.upper())
        print()
        break
    else:
        guess_word = input("Make another guess?: ") 
        guess = guess_word.lower()
        number_of_guesses = number_of_guesses + 1  


print(guess.upper())
if(number_of_guesses == 1 ):
    print(f"CONGRATS!!! You guessed it! After {number_of_guesses} attempt.")
else:
    print(f"CONGRATS!!! You guessed it! After {number_of_guesses} attempts.")
