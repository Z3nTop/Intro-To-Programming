''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  10/31/25)
Last Mod Date:  10/31/25)
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

def main():

    #Asks the user for info
    name = input("What is your name? ")
    collage = input("What collage are you going to? ")
    major = input("What is your major? ")
    gYear = input("What is your expected graduation year? ")
    hobs = input("and a sentence describing their hobbies and/or interests. ")
    
    writeBiography(name, collage, major, gYear, hobs)

def writeBiography(name, collage, major, gYear, hobs):

    outputFile = open("biography.html", 'w')

    #Makes the HTML code
    outputFile.write("<html>" + "\n")
    outputFile.write(f"<head><title>" + collage + " student " + name + "</title></head>" + "\n")
    outputFile.write("<body>" + "\n")
    outputFile.write(f"<center><h1>{name}</h1></center>" + "\n")
    outputFile.write(f"<hr />" + "\n")
    outputFile.write(f"My name is {name}. I am a {major} major at {collage}. I expect to graduate in {gYear}." + "\n")
    outputFile.write("<br /><br />" + "\n")
    outputFile.write(f"{hobs}" + "\n")
    outputFile.write("<hr/>" + "\n")
    outputFile.write("</body>" + "\n")
    outputFile.write("</html>")

    outputFile.close()

#Calls main
if __name__ == "__main__":
    main()
