# Chapter 8 Lab - Pig Latin Translator

def main():
    print("Pig Latin Translator\n")
    print("This program translates the contents of a text file to Pig Latin.\n")

    while True:
        try:
            # Get file path from user
            filePath = input("File path: ")

            # Attempt to open and read contents of specified file and
            # Split the text into a list based on newline character (each line of text becomes an element in list)
            linesList = readFile(filePath).split("\n")
        except Exception as ex:
            # If there is an error opening file
            print(ex)
        else:
            break       # Exit loop if there are no problems
        # end try
    # end while

    # Translate and add each line to translated list
    translatedLinesList = []
    for line in linesList:
        translatedLinesList.append(translateLineToPigLatin(line))
    # end for

    try:
        # Determine name for translated file
        periodIndex = filePath.rfind(".")
        translatedFilePath = filePath[:periodIndex] + "PigLatin" + filePath[periodIndex:]

        # Write translation to file
        print("\nTranslating...")
        writeFile(translatedFilePath, translatedLinesList)
        print("Translated file written to", translatedFilePath)
    except Exception as ex:
        # If there is an error writing file
        print(ex)
    # end try
# end function


def readFile(filePath):
    try:
        # Open file path for reading
        fileObject = open(filePath, "r")

        # Read all lines from file
        fileContents = fileObject.read()
    except FileNotFoundError:
        raise FileNotFoundError("Unable to open file: the specified file does not exist.")
    except:
        raise Exception("An unexpected problem occurred whilst opening the file.")
    else:
        fileObject.close()

        return fileContents
    # end try
# end function


def writeFile(filePath, linesList):
    try:
        # Open file path for writing
        fileObject = open(filePath, "w")

        # Ensure there is at least 1 item in list
        if len(linesList) > 0:
            # Process each line of text in list
            for line in linesList:
                # Write each translated line to file
                fileObject.write(line)
            # end for
        else:
            raise Exception("Unable to translate: the file does not contain any text.")
        # end if
    except:
        raise Exception("An unexpected problem occurred whilst writing the file.")
    else:
        fileObject.close()
    # end try
# end function

def translateLineToPigLatin(line):
    translatedLine = ""

    # If line has one or more character
    if len(line) > 0:
        # If line ends with a newline character, remove it
        if line.endswith("\n"):
            line = line.rstrip("\n")
        # end if

        # Split line into a words list based on a space
        wordList = line.split(" ")

        # Concatenate each translated word with a trailing space to translatedLine
        for word in wordList:
            translatedLine += translateWordToPigLatin(word) + " "
        # end for
    # end if

    return translatedLine + "\n"    # Return translated line with trailing newline character
# end function


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

    #All letters after the first
    wordRest = word[1: len(word)]

    #Removes Punc if word has one
    if endsWithPunc:
        wordRest = wordRest[0: len(wordRest)-1]
        punctCh = lastCh


    #checks if the starting letter is a vowl or a cons
    if (lowStart in vol):
        if endsWithPunc:
            pigLatinWord = wordRest + "yay" + punctCh
        else:
            pigLatinWord = wordRest + "yay"
    elif (lowStart in cons):
        if endsWithPunc:
            pigLatinWord = wordRest + lowStart + "ay" + punctCh
        else:
            #Takes the given word and convers to piglatin using cons rules
            pigLatinWord = wordRest + lowStart + "ay"

        #Checks if the word starts with a Cap and sets it when covered
        if startIsCap:
            pigLatinWord = pigLatinWord[0].upper() + pigLatinWord[1:len(pigLatinWord)]
    else:
        pigLatinWord = word

    return pigLatinWord
# end function





# DO NOT MODIFY CODE BELOW THIS LINE
if __name__ == "__main__":
    main()
# end if
