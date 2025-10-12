''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  10/1/25)
Last Mod Date:  10/1/25)
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
#inports random and sets random number for the guess
import random
number = random.randint(1, 20)





isRunning = True
while isRunning:
    print(number)
    guess = int(input("What is your guess? "))
    if guess == number:
        isRunning = False


print("Your lifelong dream is to be on the Jedi Council")
print("Your opportunity comes and you get an interview with Yoda.")
print("He asks you to guess a number between 1 and 20.")

'''
Your lifelong dream is to be on the Jedi Council.  
Your opportunity comes and you get an interview with Yoda. 
He asks you to guess a number between 1 and 20.  
You need to write a program that creates a random number from 1 to 20 and then asks a guess from the user.  
If the guess is higher than the random number then you need to display “Too High, Guess Again!”  
If the guess is lower than the random number you need to display “Too Low, Guess Again!”  
The program should keep asking until the number is guessed. Once the number is guessed, you need to display 
“Congratulations, been accepted to the Jedi Council you have ” only if the user number of guesses are 3 or less.
If the number of guesses is more than 3 then print “Ready for the Jedi Council you are not. Weak with the force you are!”
'''
