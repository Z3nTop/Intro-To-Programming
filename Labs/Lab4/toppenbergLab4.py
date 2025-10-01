''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab4
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  9/28/25)
Last Mod Date:  10/1/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - to add all given numbers tht aren't 67
-----------------------------------------------------------------------------
Description of input:
Numbers to be add together
Description of output:
Adds all of the given number added together
-----------------------------------------------------------------------------
'''
#sets vars for the program
num = 0
tottal = 0

#Asks the user for numbers and will keep going until the user inputs 67
while num != 67:
    num = int(input("Enter a positive number… enter 67 to end the program: "))
    if num < 0:
        print("Must me a postive number")
#This part stops the negetice number form beinging added to the tottal
        num = 0
    tottal += num
    

#Prints the sum of all numbers given munus 67
print("The sum of the numbers is", tottal-67)
