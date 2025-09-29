''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab4
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  9/28/25)
Last Mod Date:  9/29/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <general description of program's purpose>
-----------------------------------------------------------------------------
Description of input:
Numbers to be add together
Description of output:
Adds all of the given number
-----------------------------------------------------------------------------
'''
#sets vars for the program
num = 0
tottal = 0


#Takes the user input and adds it to it's self
while num != 67:
    num = int(input("Enter a positive number… enter 67 to end the program: "))
    if num < 0:
        print("Must me a postive number")
    tottal += num
    

#Need to find a better way to do this
#Also need to fix that non postive numbers being added
print(tottal-67)

'''
Write a program that asks the user to enter a positive number.  The program should check to see if the user entered a negative number and respond accordingly. The program should use a WHILE loop to keep asking the user to enter a number or enter 67 to stop (This will be the Sentinel that terminates your program). Your while loop should keep a running total (sum) of the numbers entered by the user (except if they enter 67). 67 shouldn’t be added.  

Sample Input
Write a program that asks the user to enter a positive number.  The program should check to see if the user entered a negative number and respond accordingly. The program should use a WHILE loop to keep asking the user to enter a number or enter 67 to stop (This will be the Sentinel that terminates your program). Your while loop should keep a running total (sum) of the numbers entered by the user (except if they enter 67). 67 shouldn’t be added.  

Sample Input
Enter a positive number… enter 67 to end the program:  3
Enter a positive number… enter 67 to end the program:  8 
Enter a positive number… enter 67 to end the program:  67
The Sum of the numbers entered is:  11:  3
Enter a positive number… enter 67 to end the program:  8 
Enter a positive number… enter 67 to end the program:  67
The Sum of the numbers entered is:  11
'''