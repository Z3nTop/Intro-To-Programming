''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  10/20/25)
Last Mod Date:  10/22/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - Gives random stats for a character
-----------------------------------------------------------------------------
Description of input:
NONE
Description of output:
The sheet with random stats to character.txt
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
    
    #opens the file for writing
    outfile = open('character.txt', 'w')

    #Outputs the random stats to the file
    outfile.write("Strength   "  + str(strength)+ "\n")
    outfile.write("constitution   "  + str(constitution)+ "\n")
    outfile.write("wisdom   "  + str(wisdom)+ "\n")
    outfile.write("dexterity   "  + str(strength)+ "\n")
    outfile.write("charisma   "  + str(charisma)+ "\n")

    #closes the file
    file.close()


#Calls main
if __name__ == "__main__":
    main()