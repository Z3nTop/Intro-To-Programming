''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab1
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  9/3/25
Last Mod Date:  9/3/25
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - Ask the user for indomation about thier character
-----------------------------------------------------------------------------
Description of input:
<short description of program's inputs>
Description of output:
<short description of program's outputs>
-----------------------------------------------------------------------------
'''

#Askes the user for infoamtuon about thier charater

print("Wellcome to the world of DND")
name = input("Let's start with your name ")
level = int(input("What level are you? "))
hp = int(input("How many hit points do you have? "))
gold = int(input("How much gold do you have? "))

#display the charoter info
print("Here is your character sheet")
print("Name:", name)
print("Level:", level)
print("Hit points: ", hp)
print("Gold: ", gold)