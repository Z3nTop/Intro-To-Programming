''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  10/20/25)
Last Mod Date:  10/20/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - Gives random stats for a character
-----------------------------------------------------------------------------
Description of input:
NONE
Description of output:
The sheet with random stats
-----------------------------------------------------------------------------
'''

def main():
    #Inports random
    import random


    #Set the starts for the character starts
    strength = random.randint(1, 18)
    constitution = random.randint(1, 18)
    wisdom = random.randint(1, 18)
    dexterity = random.randint(1, 18)
    charisma = random.randint(1, 18)
    

    outfile = open('character.txt', 'w')

    
    outfile.write("Strength   "  + str(strength)+ "\n")
    outfile.write("constitution   "  + str(constitution)+ "\n")
    outfile.write("wisdom   "  + str(wisdom)+ "\n")
    outfile.write("dexterity   "  + str(strength)+ "\n")
    outfile.write("charisma   "  + str(charisma)+ "\n")




#Calls main
if __name__ == "__main__":
    main()


""""
Write a program that creates a character.txt file and writes to it (On its own line) 
the word Strength, Constitution,  Wisdom, Intelligence, Dexterity and Charisma. 
After each word you need place a RANDOM number from 1 to 18 for each attribute. 
So the file should have something like this:

Strength 12
Constitution 13
Wisdom 9
Dexterity 9
Charisma 18
REMEMBER each time I run your program it should create a new character.txt file with difference random numbers
"""
