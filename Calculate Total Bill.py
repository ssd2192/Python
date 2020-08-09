#This program calculate the total price
#This program uses funtions and while condition and if condition

#the main function
def main():
    endProgram, endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount = declareVariable()

    while endProgram == 'no':
        endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal = resetVariables()
        while endOrder== 'no':
            print ("Enter 1 for Yum Yum Burger")
            print ("Enter 2 for Grease Yum Fries")
            print("Enter 3 for Soda Yum")
            option=int(input("Enter option: "))
            if option == 1:
                totalBurger = getBurger(totalBurger)
            elif option == 2:
                totalFry = getFry(totalFry)
            elif option == 3:
                totalSoda = getSoda(totalSoda)
            endOrder = input("Do you want to end your order?(Enter no to add more items: )")
        total = calcTotal(totalBurger, totalFry, totalSoda)
        printReceipt(total)
        endProgram = input("Do you want to end the program? (Enter no to process a new order)")

#this funtion initialize the variables
def declareVariable():
    endProgram = "no"
    endOrder = "no"
    totalBurger = 0
    totalFry = 0
    totalSoda = 0
    total = 0
    tax = 0
    subtotal = 0
    option = 0
    burgerCount = 0
    fryCount = 0
    sodaCount = 0
    return endProgram, endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount

#this function reset variables for new customer
def resetVariables():
    endOrder = "no"
    totalBurger = 0
    totalFry = 0
    totalSoda = 0
    total = 0
    tax = 0
    subtotal = 0
    return endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal

def getBurger(totalBurger):
    burgerCount = float(input("Enter the number of burgers you want"))
    totalBurger +=burgerCount*.99
    return totalBurger

def getFry(totalFry):
    fryCount = float(input("Enter the number of Fries you want"))
    totalFry += fryCount*.79
    return totalFry

def getSoda(totalSoda):
    sodaCount = float(input("Enter the number of sodas you want"))
    totalSoda += sodaCount*1.09
    return totalSoda

def calcTotal(totalBurger, totalFry, totalSoda):
    subtotal = totalBurger + totalFry + totalSoda
    tax = subtotal*.06
    total = subtotal + tax
    return total

#this function prints the total price of order
def printReceipt(total):
    print("Your total is $", total)

#calls main
main()
