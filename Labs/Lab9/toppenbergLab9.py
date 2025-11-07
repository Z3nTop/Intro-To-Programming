''' 
-----------------------------------------------------------------------------
Solution:       toppenbergLab
-----------------------------------------------------------------------------
Developer:      Zen Toppenberg
Course:         Intro to Programming & Logic – CITC-1301-H91
Creation Date:  11/7/25)
Last Mod Date:  11/7/25)
E-mail Address: nxtoppenberg@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - Givs the user the total, avgaeage lowest and hight of the bills for the year
-----------------------------------------------------------------------------
Description of input:
How much you piaded every month
Description of output:
<short description of program's outputs>
-----------------------------------------------------------------------------
'''
def main():
    #Imports
    import math
    import numpy

    #asks the user how much was sepnt each month
    jan = float(input("Enter the grocery bill for Jan "))
    feb = float(input("Enter the grocery bill for Feb "))
    mar = float(input("Enter the grocery bill for Mar "))
    apr = float(input("Enter the grocery bill for Arp "))
    may = float(input("Enter the grocery bill for May "))
    jun = float(input("Enter the grocery bill for Jun "))
    jul = float(input("Enter the grocery bill for Jul "))
    aug = float(input("Enter the grocery bill for Aug "))
    sep = float(input("Enter the grocery bill for Sep "))
    oct = float(input("Enter the grocery bill for Oct "))
    nov = float(input("Enter the grocery bill for Nov "))
    des = float(input("Enter the grocery bill for Des "))

    year_total = sum((jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, des))
    year_ave   = numpy.average((jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, des))
    year_low   = min((jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, des))
    year_max   = max((jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, des))

    #prints the aboutmnet spent along with the lower and chaepest month
    print(f'you spent {year_total} this year')
    print(f'Your avage amont spent was {year_ave:.02}')
    print(f'your hightest month was {year_max}')
    print(f'your cheapest month was {year_low}')


#Calls main
if __name__ == "__main__":
    main()


''''
Design a program that lets the user enter their grocery bill for each of the 12 months into a LIST. 
The program should calculate and display the total grocery bill for the year, the average grocery bill, 
the months with the highest and lowest grocery bill.  
Below is a SAMPLE input from the user of your program:



Enter the grocery bill for January: 450
Enter the grocery bill for February: 505
Enter the grocery bill for March: 400
Enter the grocery bill for April: 135
Enter the grocery bill for May: 100
Enter the grocery bill for June: 200
Enter the grocery bill for July: 250
Enter the grocery bill for August: 500
Enter the grocery bill for September: 250
Enter the grocery bill for October: 100
Enter the grocery bill for November: 125
Enter the grocery bill for December: 505
Total grocery bill: $3520.00
Average grocery bill: $293.33
Highest grocery bill: February
Lowest grocery bill: May
'''
