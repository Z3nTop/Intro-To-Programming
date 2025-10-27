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
#defs main
def main():







#Calls main
if __name__ == "__main__":
    main()



'''
The Canadian penny died on February 4, 2013. 
That was the last day pennies were distributed by the Royal Canadian Mint. 
Since pennies have been phased-out, retailers must adjust sales totals to multiples of 5 cents when customers pay with cash. 
Interestingly, transactions paid with credit and debit cards are still charged to the penny.
While retailers have some freedom in how this policy is implemented, most choose to round to the nearest nickel.


Write a Python program that reads in a series of item prices from the user until they enter the sentinel value, -1. 
Output the total cost of all entered items on one line if the customer pays with debit or credit. 
On the next line, output the amount due if the customer pays with cash (rounded to the nearest nickel). Round all outputs to two decimal places.
=
One way to calculate a cash payment is to begin by determining how many pennies would be needed to pay a total. Then, calculate the remainder when this number of pennies is divided by 5. 
Finally, adjust the total down if the remainder is less than 2.5; otherwise, adjust the total up.



Example outputs:
This program calculates the total cost of a series of items based on the Canadian payment method.
Enter -1 to stop entering item prices.

Item 1: $ 1.01 [ENTER]
Item 2: $ 1.02 [ENTER]
Item 3: $ -1 [ENTER]

Credit/debit: $2.03
Cash: $2.05






'''