''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  10/25/25)
Last Mod Date:  10/28/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - add all of them given prices and show a price for cash or card payments
-----------------------------------------------------------------------------
Description of input:
the price of items
Description of output:
the total of all prices given and rounded to .05 for cash
-----------------------------------------------------------------------------
'''

#Defines Main
def main():
    #Sets the vars to start
    total = 0
    item_num = 1
    price = 0
    looping = True

    #Starts a try for erroe checking
    try:

        #Asks the user for the price of the itmes
        print("Put in the price of your itmes when you are done type -1")
        while looping:

            #Starts a loop adding the price to total and adds one to the item number
            price = float(input("Item"f'{item_num}'": "))
            if price == -1:
                looping = False
            total = total + price
            item_num += 1

        #Bandaid fix for the -1 being added to the total
        total += 1

        #Set the price for cash and card payment
        card = round(total, 2)
        cash = round(total / 0.05) * 0.05
        cash = round(cash, 2)

        #Printes the price of all the items witout the round up down to 2 desmess
        print("Debit/Credit Price:", card) 

    #prints an eroor message if text is given for price
    except:
        print("error try agian")

#Calls main
if __name__ == "__main__":
    main()
