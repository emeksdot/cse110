"""
An adventure game created by Emeka Thomas Onwugbonu
on the 14th of March, 2024
"""
# To help with the smooth execution of the program, I added three variables namely; first, second, and third to store the responses from the user.
# I invited my teenage kids to play the game they had fun with it.


first = input("You are on your way to see a friend living in the next village. The route to your friend's house leads through a dark forest. You have to choose to go with a MATCH or  FLASHLIGHT. Which do you choose?: ")

if(first.lower() == 'match' ):
    second = input("You move with the match to the edge of the forest. As you enter the forest it is dark around you, you strike the match, and it lights your path for a few meters. Then you see two shining spots and suspect they can only be the eyes of a Tiger. Do you RUN or SCREAM?: ")

    if(second.lower() == 'run'):
        third = input("As you are running for dear life, along the way you realize that just some few meters ahead there was a fork in the path, and you have to go either to the RIGHT or the LEFT. Which way do you choose?: ")

        if(third.lower() == 'right'):
            print("You see a clearing, and in the middle of the clearing a small house with a red roof. And beyond the house, you see the the king's palace and to the rightmost part of the palace, lo and behold; your friend's house.")
            print(f"Congrats you made it!!!")

        elif(third.lower() == 'left'):
            print(f"After 2 hours of walking in the forest, you realise that you are on the wrong path, and must have to retrace your way back to the fork in the road to take the right path.")
        else:
            print(f"The sun is setting fast, do you want to sleep here?")
    elif(second.lower() == 'scream'):
        third = input("As you were screaming your head off, the noise scares off some wild birds in the under brush and in their haste to escape they knock over some objects and you could hear a distinct sound that could only come from glass bottles striking each other. You approach the spot you heard the sound, only to find out that there bottles on the ground and it was these that had reflected your match light back to you. Do you SIGH or LAUGH?: ")

        if(third.lower() == 'sigh'):
            print("I think I should go back home.")
        elif(third.lower() == 'laugh'):
            print(f"I have not laughed this hard in a really long while. Let me continue my journey.")
        else:
            print(f"Be honest, were you scared or not?")    
    else:
        print(f"Don't tell me you feel no emotions, because I won't believe you.")    

elif (first.lower() == 'flashlight' ):
    second = input("You carry the flashlight to the edge of the forest. As you enter the forest it is dark around you, you switch on the flashlight, it bathes your path with light for up to 10 meters in whichever way you point it to. As you are walking along, you heard a noise directly overhead and you decided to see what's making the noise. As you direct the beams upward, you stare right into the eyes of an owl perched on a tree. Do you CONTINUE or RETURN?: ")

    if(second.lower() == 'continue'):
        third = input("You are feeling brave today and will not be scared by any owl. After an hour you get to the end of the forest track where the only means of transport is riding a donkey into your friends village. Going on foot will afford you enough time to take in the scenery of the countryside. Do you go by FOOT or ride the DONKEY?: ")

        if(third.lower() == 'foot'):
            print(f"Enjoy the view.")
        elif(third.lower() == 'donkey'):
            print(f"Get ready for a bumpy ride!")            
        else:
            print(f"You can stay here by your self all day, aren't you going into your friend's village again?")

    elif(second.lower() == 'return'):
        third = input("I am feeling uneasy about continuing this trip. I think I should get a souvenir to remember this failed trip. I see some wild roses, which color should I pick, RED or YELLOW or WHITE?: ")

        if(third.lower() == 'red'):
            print(f"I didn't loose my mind after all.")
            print(f"I think I would replan this trip.")
        elif(third.lower() == 'yellow'):
            print(f"I feel mellow.")
            print(f"I think I would better postpone this trip.")
        elif(third.lower() == 'white'):
            print(f"I am coming back home in peace.")
        else:
            print(f"You didn't pick any roses, why?")

    else:
        print(f"It's either you continue the journey or you return home. Which will it be?")

else:
    print(f"You need a means of overcoming the darkness inside the forest. Go back and make a choice of what to use, right now!")
