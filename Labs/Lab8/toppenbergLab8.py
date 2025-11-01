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
        fileName = "biography.html"

        #Asks the user for info and cecks for info
        name = input("What is your name? ")
        while len(name) == 0:
            name = input("Must enter 1 letter or more ")

        collage = input("What collage are you going to? ")
        while len(collage) < 2:
           collage = input("Must enter 2 letter or more ")

        major = input("What is your major? ")
        while len(major) < 2:
           major = input("Must enter 2 letter or more ")

        gYear = input("What is your expected graduation year? ")
        while len(gYear) < 4 or len(gYear) > 4:
            gYear = input("Must use 2000 year format ")

        hobs = input("and a sentence describing your hobbies or interests. ")

        writeBiography(fileName, name, collage, major, gYear, hobs)



def writeBiography(fileName, name, collage, major, gYear, hobs):

        try:
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

            #closes the file
            outputFile.close()
        except:
            pirnt("You did somthing wrong try agian")

 



#Calls main
if __name__ == "__main__":
    main()
