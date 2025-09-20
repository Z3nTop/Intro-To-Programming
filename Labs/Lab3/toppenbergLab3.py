''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab3
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  9/19/25)
Last Mod Date:  9/19/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - doubles $100 for every year money is kept in the stock matket
-----------------------------------------------------------------------------
Description of input:
Number of years the user will play the stock market
Description of output:
How much money the user will have in the number of years
-----------------------------------------------------------------------------
'''
#ask user for input
print("You have $100 and want to play the stock market")
years = int(input("How many years do you want to keep your money in it? "))


#Checks if years is less then zero
if years == 0:
    print("yeah the stock market is just too risky anyway")
elif years <= 0:
    print("Time mechine not found")

#sets the vars for loops and money
money = 100
loops = 0

#first checks if years is more then zero then loops and doubles money for every year
if years > 0:
    print ("Years  Total")
    print("------------")
    #takes the users input and doubles the money for every year
    while loops < years + 1:
        print(loops, "$",money)
        money *= 2
        loops += 1

