''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  10/6/25)
Last Mod Date:  10/7/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - Converts human years to dog years useing funtions
-----------------------------------------------------------------------------
Description of input:
<short description of program's inputs>
Description of output:
<short description of program's outputs>
-----------------------------------------------------------------------------
'''

# Lab3 - Human to Dog Years

# Constants
FIRST_YEAR_EQUIV = 15
SECOND_YEAR_EQUIV = 9
THREE_PLUS_YEARS_MULTIPLIER = 5



# Output program's purpose
print("This program calculate's a dog's approximate age in \"dog years\" based on human years.\n")

# Get human years from user
def getDogYears(humanYears):
    # Human age to dog age calculation
    if humanYears <= 1:
        dogYears = FIRST_YEAR_EQUIV * humanYears
    elif humanYears <= 2:
        dogYears = FIRST_YEAR_EQUIV + SECOND_YEAR_EQUIV * (humanYears - 1)
    else:
        dogYears = FIRST_YEAR_EQUIV + SECOND_YEAR_EQUIV + THREE_PLUS_YEARS_MULTIPLIER * (humanYears - 2)
    return dogYears


def main():
    #Asks the user for the Dogs age in human years
    humanYears = float(input("Dog's age in human years? "))
    #Checks if the given input is a postive number
    while humanYears < 0:
        humanYears = float(input("\nHuman age must be a positive number. "))
    #Converts humans to dogs years using the funtion
    calculatedDogYears = getDogYears(humanYears)
    #Outputs the converted number of years
    print("\nA dog with a human age of", format(humanYears, ",.1f"), "years is", 
        format(calculatedDogYears, ",.1f"), "in dog years.")
# end if

#Sets var for while loop
loops = True


#Starts a loop for the program to 
while loops:
    main()
    testRepeat = True
    while testRepeat:
        ask = input("Do you want to convert again? y/n ")
        if ask == "y" or ask =="Y":
            loops = True
            testRepeat = False
        elif ask == "n" or ask == "N":
            loops = False
            testRepeat = False
        else:
            print("what? ")