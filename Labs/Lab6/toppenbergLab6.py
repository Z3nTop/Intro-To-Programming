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
def main():
    #inports random and sets random number for the guess
    import random
    answer = random.randint(1, 20)
    guesses = 0


    #Displays the starting text
    print("Your lifelong dream is to be on the Jedi Council")
    print("Your opportunity comes and you get an interview with Yoda.")
    print("He asks you to guess a number between 1 and 20.")


    #Runs a check to see if the guessed number is the numbere that was genatraed 
    isRunning = True
    while isRunning:
        guess = int(input("What is your guess? "))
        guesses += 1
        if guess == answer:
            isRunning = False
        elif guess > answer:
            print("Your guess is too high")
        else:
            print("Your guess is too low")

    #Runs the different messages based on the number of guess is
    if guesses <= 3:
        print("Congratulations, been accepted to the Jedi Council you have")
    else:
        print("Ready for the Jedi Council you are not. Weak with the force you are!")


#Calls the mian functions
if __name__ == '__main__':
    main()


