''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  10/1/25)
Last Mod Date:  10/15/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - generates a number from 1-20 and has user guess it
-----------------------------------------------------------------------------
Description of input:
Guessed at what the number is
Description of output:
Tells the user if the guessed number is higher, lower or the curret number
-----------------------------------------------------------------------------
'''
def main(guesses):
    #inports random and sets random number for the guess
    import random
    answer = random.randint(1, 20)
    guesses = 0

    print("Your lifelong dream is to be on the Jedi Council")
    print("Your opportunity comes and you get an interview with Yoda.")
    print("He asks you to guess a number between 1 and 20.")


    #Runs a check 
    isRunning = True
    while isRunning:
        #REWMOVE BEFORE SUMMINTING 
        print(answer)
        guess = int(input("What is your guess? "))
        if guess == answer:
            isRunning = False
            guesses += 1
        elif guess > answer:
            print("Your guess is too high")
            guesses += 1
        else:
            print("Your guess is too low")
            guesses += 1
    return guesses


main(guesses)

#Runs the different messages based on the number of guess is
if guesses <= 3:
    print("Congratulations, been accepted to the Jedi Council you have")
else:
    print("Ready for the Jedi Council you are not. Weak with the force you are!")


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
