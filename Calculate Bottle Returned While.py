#This program calculate the bottles returned in a week
#This program uses funtions and while condition

#the main function
def main():
    endProgram = 'no'
    while endProgram == 'no':
        totalBottles = getBottles()
        totalPayout = calcPayout(totalBottles)
        printInfo(totalBottles,totalPayout)
        endProgram = input("Do you want to end the program? (Enter yes or no):")

#this funtion will inputs bottles for a week
def getBottles():
    totalBottles = 0
    todayBottles = 0
    counter = 1
    while counter<=7:
        todayBottles = int(input("Enter number of bottles for today: "))
        totalBottles = totalBottles + todayBottles
        counter = counter + 1
    return totalBottles

#this function will calculate payment for the bottles returned
def calcPayout(totalBottles):
    totalPayout = 0
    totalPayout = totalBottles * .10
    return totalPayout

#this function prints the number of bottles returned and price paid
def printInfo(totalBottles, totalPayout):
    print ("The total number of bottles collected is", totalBottles)
    print ("The total paid out is $", totalPayout)

#calls main
main()
