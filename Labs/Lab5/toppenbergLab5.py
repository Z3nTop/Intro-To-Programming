''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  10/6/25)
Last Mod Date:  10/6/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <general description of program's purpose>
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
humanYears = float(input("Dog's age in human years? "))

if humanYears < 0:
    print("\nHuman age must be a positive number.")
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
