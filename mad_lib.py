"""
A Mad Lib program created by Emeka Thomas Onwugbonu
on March 2, 2024
"""
# I added the following variables to the story
# second_adjective, place, second_animal, second_verb, sound 

adjective = input("Choose an adjective: ")
animal = input("Choose an animal: ")
verb = input("Choose a verb: ")
exclamation = input("Enter an exclamation: ")

second_adjective = input("Choose superlative adjective: ")
place = input("Choose a place: ")
second_animal = input("Choose another animal: ")
second_verb = input("Choose the past tense of a verb: ")
sound = input("Choose any sound you like: ")

if(second_animal[0] in "aeiou"):
    article = "an"
else: 
    article = "a"


print(f"The other day, I was really in trouble. It all started when I saw a very \n{adjective} {animal} {verb} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all \nI could think to do was to {verb} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb} \nright in front of my family.\nAt the {place}, there is {article} {second_animal}, it is the {second_adjective} animal \nI have ever {second_verb} while visiting the {place}. The only sound \nanyone has ever heard it make is \"{sound.capitalize()}! {sound.capitalize()}!! {sound.capitalize()}!!!\"  ")