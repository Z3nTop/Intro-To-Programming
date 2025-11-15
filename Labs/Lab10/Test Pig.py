def main():
    
    while True:
        x = input("Type anything: ")
        print(translateWordToPigLatin(x))

def translateWordToPigLatin(word):
    #Sets indexes for vowels and cons
    vol = ["a", "e", "i", "o", "u", "y"]
    cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    punct = (".", ",", ":", ";", "?", "!")


    
    #The first letter of a word
    wordStart = word[0]

    #Make first letter lower case
    lowStart = wordStart.lower()
    
    #The word starts up with upper case
    startIsCap = (wordStart != lowStart)

    #The last letter of the word
    lastCh = (word[len(word)-1])

    #Checks if the word ends with a punc
    endsWithPunc = word.endswith(punct)
    punctCh = ""

    #All letters after the first
    wordRest = word[1: len(word)]

    #Removes Punc if word has one
    if endsWithPunc:
        print("Before:", wordRest)
        wordRest = wordRest[0: len(wordRest)-2]
        print("-->", wordRest)
        punctCh = lastCh


    #checks if the starting letter is a vowl or a cons
    if (lowStart in vol):
        if endsWithPunc:
            pigLatinWord = wordRest + "yay" + punctCh
        else:
            pigLatinWord = word + "yay"
    elif (lowStart in cons):
        if endsWithPunc:
            pigLatinWord = wordRest + "ay" + punctCh
        else:
            #Takes the given word and convers to piglatin using cons rules
            pigLatinWord = wordRest + lowStart + "ay"

        #Checks if the word starts with a Cap and sets it when covered
        if startIsCap:
            pigLatinWord = pigLatinWord[0].upper() + pigLatinWord[1:len(pigLatinWord)]
    else: 
        pigLatinWord = word
    
    return pigLatinWord		# !!TO DO!!
# end function

main()