''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab2
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  9/12/25)
Last Mod Date:  9/15/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - Convert human years to dog years
-----------------------------------------------------------------------------
Description of input:
asks for a number of human years to be converted to dog years
Description of output:
Outputs the number of human years converted to dog years
-----------------------------------------------------------------------------
'''
#ask the user for an input for human years
human_years = float(input("enter the number of human years to converte to dog years "))

#Convets the number of human years to dog years
if human_years < 0:
    print("Error input can not be less then 0")
else:
    if human_years <= 1:
            dog_years = 15 * human_years
    elif human_years <= 2:
            dog_years = 15 + 9 * (human_years - 1)
    else: 
            dog_years = 15 + 9 + 5 * (human_years - 2)
    print(human_years, "would be", dog_years, "in dog years")
