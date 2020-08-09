"""This program will take in monthly sales and sales increase from the user then
calculate and display the store bonus and employee bonus"""

#Declaration and calling
def main():
    monthlySales= getSales()
    salesIncrease= getIncrease()
    storeAmount= storeBonus(monthlySales)
    empAmount= empBonus(salesIncrease)
    printBonus(storeAmount,empAmount)

#This function accept monthly sales from user
def getSales():
    monthlySales = float(input("Enter your monthly sales "));
    return monthlySales;

#This function accept sales increase from the user
def getIncrease():
    salesIncrease = float(input("Enter percent of sales increase. For example, 4% should be entered as 4 "))
    salesIncrease /= 100
    return salesIncrease;

#this function compare monthly sales and initialize store amount
def storeBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount;

#this function compare sales increase and initialize employee amount
def empBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount;

#this function prints the calculated values
def printBonus(storeAmount,empAmount):
    print ("The store bonus amount is $",storeAmount)
    print ("The employee bonus amount is $", empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print ("Congrats! You have reached the heighest bonus amounts possible!")

main()
