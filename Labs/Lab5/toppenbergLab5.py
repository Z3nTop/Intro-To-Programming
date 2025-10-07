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

def getDogYears():
    humanYears = float(input("Dog's age in human years? "))

    while humanYears < 0:
        humanYears = float(input("\nHuman age must be a positive number. "))
        
    else:
        # Human age to dog age calculation
        if humanYears <= 1:
            dogYears = FIRST_YEAR_EQUIV * humanYears
        elif humanYears <= 2:
            dogYears = FIRST_YEAR_EQUIV + SECOND_YEAR_EQUIV * (humanYears - 1)
        else:
            dogYears = FIRST_YEAR_EQUIV + SECOND_YEAR_EQUIV + THREE_PLUS_YEARS_MULTIPLIER * (humanYears - 2)
        # end if

        print("\nA dog with a human age of", format(humanYears, ",.1f"), "years is", 
            format(dogYears, ",.1f"), "in dog years.")
# end if

getDogYears()


'''
Given task
Start with the solution for Chapter 3 Project (or by copying/pasting the code below into an editor). Modify the "Human to Dog Years" program with the following enhancements:
    • If the user enters a value less than zero for humanYears, use a loop to inform the user that "Human years must be a positive number" and ask the user to enter humanYears again (until the user enters an acceptable value).
    • Move the logic used to determine the human years to dog years calculation into a function, called: getDogYears(). The getDogYears() function accepts one floating-point argument, called: humanYears. Based on the passed-in humanYears argument, the getDogYears() function calculates and returns the equivalent age in dog years as a floating-point value (i.e., the function should not return a string). 
Note: Do not output anything to the screen from the getDogYears() function! Output to screen should only occur from the main() function.
    • Use a loop to allow the user to calculate another human to dog years if they so choose.
Human To Dog Years program source code
'''
