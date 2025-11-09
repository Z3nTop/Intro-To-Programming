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
Purpose - To give the amount paid in grocery along wiht the avge and moths you paid the most and leas
-----------------------------------------------------------------------------
Description of input:
How much you piaded every month
Description of output:
Givs the user the total, avgaeage lowest and hight of the bills for the year
-----------------------------------------------------------------------------
'''
def main():

    #Makes a list for the amoubnt piad
    user_data = []
    #Makes in index for every month
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    #Starts a loop to check if the user gave a vaid input
    for month in months:
        looping = True
        while looping:
            try:
                amount = float(input(f"Enter the grocery bill for {month} "))
                looping = False
            except:
                print("Invalid input, please try again...")
                
        user_data.append(amount)

    #gets the sum and avg pf the total prive paid for the year
    year_total = sum(user_data)
    year_ave = (year_total / len(months))

    #This finds the index number for the highest and gets the name
    year_high = months[user_data.index(max(user_data))]

    #this finds the index number for the loest and get the name
    year_low = months[user_data.index(min(user_data))]

    #prints the amount spent, avage  along with the lower and chaepest month
    print(f'You spent {year_total} this year')
    print(f'Your avage amont spent was {year_ave:.2f}')
    print(f'Your hightest month was {year_high}')
    print(f'Your cheapest month was {year_low}')


#Calls main
if __name__ == "__main__":
    main()



'''
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
